var app = app || {};

var Stock = Backbone.Model.extend({
    defaults:
    {
        Symbol: '',
        Name: '',
        historicalCSV: ''
    }
});

app.Stock = new Stock();