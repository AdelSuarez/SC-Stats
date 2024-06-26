import reflex as rx
from BS_App.state.State import State
from BS_App.components.card_stats import card_stats
from BS_App.components.stats_profile import stats_profile
from BS_App.components.button import button
from BS_App.views.brawlers import brawlers
from BS_App.views.battlelog_view import battlelog_view
from BS_App.style import style
from BS_App import constants
from BS_App.style.style import Spacing, Size, BOX_SHADOW
from BS_App.style.colors import TextColor


def profile() -> rx.Component:
    return rx.cond(
        State.info_player.is_visible,
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    rx.vstack(
                        rx.avatar(
                            src=State.info_player.icon,
                            fallback="RX",
                            size="8"
                        ),
                        rx.text(
                            f'{State.info_player.tag}',
                            color=TextColor.TERTIARY.value,
                            font_size=Size.DEFAULT.value,
                            as_="span"
                        ),
                        spacing=Spacing.ZERO.value
                    ),
                    rx.vstack(
                        rx.text(
                            f'{State.info_player.name}',
                            font_size=Size.MEDIUM_BIG.value,

                        ),
                        rx.vstack(
                            stats_profile(
                                "/trophy.png", f'{State.info_player.trophies}'),
                            stats_profile(
                                "/Info.webp", f'EXP: {State.info_player.expLevel}'),

                            rx.cond(
                                State.info_player.clubName != "",
                                stats_profile(
                                    "/Club.webp", f'{State.info_player.clubName}'),
                                stats_profile("/NoClub.webp", "Sin Club")
                            ),

                            spacing=Spacing.VERY_SMALL.value
                        ),
                        spacing=Spacing.ZERO.value,

                    ),
                ),

                rx.flex(

                    card_stats(
                        "MÁXIMO DE TROFEOS", State.info_player.highestTrophies, "Ranking.webp"),
                    card_stats("VICTORIAS 3 VS 3",
                               State.info_player.Victories3vs3, "3v3.png"),
                    card_stats(
                        "VICTORIAS EN SOLITARIO", State.info_player.SoloVictories, "Showdown.webp"),
                    card_stats(
                        "VICTORIAS EN DÚO", State.info_player.DuoVictories, "Duo-Showdown.webp"),

                    align="center",
                    justify="center",
                    spacing="2",

                ),
                style=style.box_style,
                align_items="center",  # Alinea los elementos horizontalmente al centro
            ),

            rx.hstack(
                button(constants.BTN_BRAWLER),
                button(constants.BTN_BATTLELOG),
            ),

            rx.cond(
                State.current_container == constants.BTN_BRAWLER,
                brawlers(),
                rx.cond(
                    State.current_container == constants.BTN_BATTLELOG,
                    battlelog_view(),
                ),
            ),
            align="center",
        ),
        rx.cond(
            State.message_user_void,
            # message("Error con la api"),
            # message("Error con la api"),

            rx.box(
                rx.heading('Jugador no existe', size="6",
                           font_family="Lilita One", font_weight="300",),
                bg="#E6B0AA",
                border_radius="10px",
                width="30%",
                margin="100px",
                padding="20px",
                text_align="center",
                box_shadow=BOX_SHADOW,

            ),
        ),
    )
