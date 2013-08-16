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
        this.$('.page').html(this.template(app.Stock.toJSON()));
    },

    updateStock: function() {
        var symbol = $('#symbol-field').val();
        var stock = app.Stocks.where({Symbol: symbol});
        app.Stock.set(stock[0].toJSON());
    }

});


var appView = new app.AppView();
