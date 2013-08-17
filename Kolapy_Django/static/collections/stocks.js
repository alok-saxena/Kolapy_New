var app = app || {};

var StockList = Backbone.Collection.extend({
    model: Stock,
    url: '/stocks'
});
