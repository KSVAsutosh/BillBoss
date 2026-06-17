document.addEventListener(
    "DOMContentLoaded",
    () => {

        const currentTheme =
            localStorage.getItem(
                "billboss-theme"
            );

        if (
            currentTheme === "dark"
        ) {
            document.body.classList.add(
                "dark-mode"
            );
        }

    }
);

function toggleTheme() {

    document.body.classList.toggle(
        "dark-mode"
    );

    if (
        document.body.classList.contains(
            "dark-mode"
        )
    ) {

        localStorage.setItem(
            "billboss-theme",
            "dark"
        );

    } else {

        localStorage.setItem(
            "billboss-theme",
            "light"
        );
    }
}