import { getCsrfToken } from "@utils/functions";
import { useEffect, useRef } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { api } from "../config/axios";

export function Component() {
    const location = useLocation();
    const navigate = useNavigate();
    const isEffectCalled = useRef(false);

    useEffect(() => {
        const completeOAuth = async () => {
            const params = new URLSearchParams(location.search);

            const code = params.get("code");
            const state = params.get("state");

            // If the required query parameters are missing, redirect to homepage
            if (!code || !state) {
                navigate("/");
                return;
            }

            if (code && state) {
                const storedState = sessionStorage.getItem("oauth_state");

                // Check if the state matches
                if (state !== storedState) {
                    navigate("/");
                    return;
                }

                try {
                    const csrfToken = await getCsrfToken();

                    await api.post(
                        `/auth/complete/`,
                        { code: code },
                        {
                            headers: {
                                "Content-Type": "application/json",
                                "X-CSRFToken": csrfToken,
                            },
                        }
                    );

                    // Redirect to homepage or dashboard
                    navigate("/profile");
                } catch (error) {
                    console.error("OAuth authentication failed", error);
                    navigate("/");
                }
            }
        };

        if (!isEffectCalled.current) {
            // Check if the effect was already called
            isEffectCalled.current = true;
            completeOAuth();
        }
    }, [location, navigate]);

    return <></>;
}

Component.displayName = "DiscordOAuthCallback";
