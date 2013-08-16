var app = app || {};

var Stock = Backbone.Model.extend({
    defaults:
    {
        Symbol: '',
        Name: ''
    }
});

app.Stock = new Stock({Symbol: 'AAPL', Name: 'APPLE INC.'});