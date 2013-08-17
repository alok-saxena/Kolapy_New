var app = app || {};

app.AppView = Backbone.View.extend({
    el: '.container',
    template: _.template($('#stock-view-template').html()),

    initialize: function() {
        this.listenTo(app.Stock, 'change', this.render);
    },

    events: {
        'blur #symbol-field': 'updateStock'
    },

    render: function() {
        var stock = app.Stock
        this.$('.page').html(this.template(stock.toJSON()));
        g.updateOptions({
            file: stock.get('historicalCSV'),
            labels: ['Date', 'Price']
        });
    },

    updateStock: function() {
        var symbol = $('#symbol-field').val();
        app.Stock.url = '/stocks/' + symbol;
        app.Stock.fetch();
    }

});


var appView = new app.AppView();
