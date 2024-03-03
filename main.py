import flet as ft
from deep_translator import GoogleTranslator


def main(page: ft.Page):
    page.title = "All Lanaguage Translator"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.auto_scroll = True
    page.window_min_width = 1000
    page.window_min_height = 600
    page.window_width = 1000
    page.window_height = 600
    progress_ring = ft.ProgressRing(color=ft.colors.YELLOW)
    page.add(progress_ring)
    page.update()

    def translate_func(e):
        text_input_value = txt.value
        drop_value = languages.value
        text_trans = GoogleTranslator(source="auto", target=drop_value).translate(
            text_input_value
        )
        text_output.value = text_trans
        text_output.border_color = ft.colors.GREEN
        page.update()

    def change_theme(e):
        theme_mode = page.theme_mode.value
        if theme_mode == "dark":
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    def languages_on_change(e):
        drop_value = languages.value
        txt.placeholder_text = (
            GoogleTranslator(source="auto", target=drop_value).translate(
                "Enter Your Text"
            ),
        )
        text_output.placeholder_text = (
            GoogleTranslator(source="auto", target=drop_value).translate(
                "Text Translated"
            ),
        )

        page.update()

    txt = ft.CupertinoTextField(
        border_color=ft.colors.WHITE,
        expand=True,
        multiline=True,
        hint_text=r"line1\nline2\nline3\nline4\nline5",
        max_length=1000,
        height=400,
        placeholder_text=GoogleTranslator(source="auto", target="az").translate(
            "Enter Your Text"
        ),
    )
    text_output = ft.CupertinoTextField(
        border_color=ft.colors.WHITE,
        expand=True,
        multiline=True,
        read_only=True,
        max_length=1000,
        height=400,
        placeholder_text=GoogleTranslator(source="auto", target="az").translate(
            "Text Translated"
        ),
    )
    page.floating_action_button = ft.FloatingActionButton(
        on_click=translate_func, bgcolor=ft.colors.GREEN, text="Translate", width=200
    )

    languages = ft.Dropdown(
        value="azerbaijani",
        options=[
            ft.dropdown.Option("afrikaans"),
            ft.dropdown.Option("albanian"),
            ft.dropdown.Option("amharic"),
            ft.dropdown.Option("arabic"),
            ft.dropdown.Option("armenian"),
            ft.dropdown.Option("azerbaijani"),
            ft.dropdown.Option("basque"),
            ft.dropdown.Option("belarusian"),
            ft.dropdown.Option("bengali"),
            ft.dropdown.Option("bosnian"),
            ft.dropdown.Option("bulgarian"),
            ft.dropdown.Option("catalan"),
            ft.dropdown.Option("cebuano"),
            ft.dropdown.Option("chichewa"),
            ft.dropdown.Option("chinese (simplified)"),
            ft.dropdown.Option("chinese (traditional)"),
            ft.dropdown.Option("corsican"),
            ft.dropdown.Option("croatian"),
            ft.dropdown.Option("czech"),
            ft.dropdown.Option("danish"),
            ft.dropdown.Option("dutch"),
            ft.dropdown.Option("english"),
            ft.dropdown.Option("esperanto"),
            ft.dropdown.Option("estonian"),
            ft.dropdown.Option("filipino"),
            ft.dropdown.Option("finnish"),
            ft.dropdown.Option("french"),
            ft.dropdown.Option("frisian"),
            ft.dropdown.Option("galician"),
            ft.dropdown.Option("georgian"),
            ft.dropdown.Option("german"),
            ft.dropdown.Option("greek"),
            ft.dropdown.Option("gujarati"),
            ft.dropdown.Option("haitian creole"),
            ft.dropdown.Option("hausa"),
            ft.dropdown.Option("hawaiian"),
            ft.dropdown.Option("hebrew"),
            ft.dropdown.Option("hebrew"),
            ft.dropdown.Option("hindi"),
            ft.dropdown.Option("hmong"),
            ft.dropdown.Option("hungarian"),
            ft.dropdown.Option("icelandic"),
            ft.dropdown.Option("igbo"),
            ft.dropdown.Option("indonesian"),
            ft.dropdown.Option("irish"),
            ft.dropdown.Option("italian"),
            ft.dropdown.Option("japanese"),
            ft.dropdown.Option("javanese"),
            ft.dropdown.Option("kannada"),
            ft.dropdown.Option("kazakh"),
            ft.dropdown.Option("khmer"),
            ft.dropdown.Option("korean"),
            ft.dropdown.Option("kurdish (kurmanji)"),
            ft.dropdown.Option("kyrgyz"),
            ft.dropdown.Option("lao"),
            ft.dropdown.Option("latin"),
            ft.dropdown.Option("latvian"),
            ft.dropdown.Option("lithuanian"),
            ft.dropdown.Option("luxembourgish"),
            ft.dropdown.Option("macedonian"),
            ft.dropdown.Option("malagasy"),
            ft.dropdown.Option("malay"),
            ft.dropdown.Option("malayalam"),
            ft.dropdown.Option("maltese"),
            ft.dropdown.Option("maori"),
            ft.dropdown.Option("marathi"),
            ft.dropdown.Option("mongolian"),
            ft.dropdown.Option("myanmar (burmese)"),
            ft.dropdown.Option("nepali"),
            ft.dropdown.Option("norwegian"),
            ft.dropdown.Option("odia"),
            ft.dropdown.Option("pashto"),
            ft.dropdown.Option("persian"),
            ft.dropdown.Option("polish"),
            ft.dropdown.Option("portuguese"),
            ft.dropdown.Option("punjabi"),
            ft.dropdown.Option("romanian"),
            ft.dropdown.Option("russian"),
            ft.dropdown.Option("samoan"),
            ft.dropdown.Option("scots gaelic"),
            ft.dropdown.Option("serbian"),
            ft.dropdown.Option("sesotho"),
            ft.dropdown.Option("shona"),
            ft.dropdown.Option("sindhi"),
            ft.dropdown.Option("sinhala"),
            ft.dropdown.Option("slovak"),
            ft.dropdown.Option("slovenian"),
            ft.dropdown.Option("somali"),
            ft.dropdown.Option("spanish"),
            ft.dropdown.Option("sundanese"),
            ft.dropdown.Option("swahili"),
            ft.dropdown.Option("swedish"),
            ft.dropdown.Option("tajik"),
            ft.dropdown.Option("tamil"),
            ft.dropdown.Option("telugu"),
            ft.dropdown.Option("thai"),
            ft.dropdown.Option("turkish"),
            ft.dropdown.Option("ukrainian"),
            ft.dropdown.Option("urdu"),
            ft.dropdown.Option("uyghur"),
            ft.dropdown.Option("uzbek"),
            ft.dropdown.Option("vietnamese"),
            ft.dropdown.Option("welsh"),
            ft.dropdown.Option("xhosa"),
            ft.dropdown.Option("yiddish"),
            ft.dropdown.Option("yoruba"),
            ft.dropdown.Option("zulu"),
        ],
        on_change=languages_on_change,
    )

    theme = ft.Row(
        [
            ft.Icon(name=ft.icons.LIGHT_MODE),
            ft.Switch(
                value=(True if page.theme_mode.value == "dark" else False),
                thumb_color={ft.MaterialState.SELECTED: ft.colors.BLUE},
                track_color=ft.colors.YELLOW,
                focus_color=ft.colors.PURPLE,
                on_change=change_theme,
            ),
            ft.Icon(name=ft.icons.DARK_MODE),
        ]
    )

    lv = ft.ListView(auto_scroll=True)
    lv.controls.append(
        ft.Column(
            [
                languages,
                ft.Row([txt, ft.Container(width=10), text_output]),
                theme,
            ]
        )
    )
    page.add(lv)
    page.remove(progress_ring)
    page.update()


ft.app(target=main)
