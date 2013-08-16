var app = app || {};

var StockList = Backbone.Collection.extend({
    model: Stock,
    url: '/stocks'
});

app.Stocks = new StockList();
app.Stocks.fetch({
    success: function(stocks) {
        console.log(stocks.models.length);
    }
});