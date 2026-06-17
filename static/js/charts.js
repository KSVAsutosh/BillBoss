function createFinanceChart(
    elementId,
    income,
    expense
) {

    const ctx = document
        .getElementById(elementId);

    if (!ctx) return;

    new Chart(ctx, {

        type: 'doughnut',

        data: {

            labels: [
                'Income',
                'Expense'
            ],

            datasets: [{
                data: [
                    income,
                    expense
                ]
            }]
        },

        options: {
            responsive: true
        }
    });
}