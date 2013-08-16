var app = app || {};

app.AppView = Backbone.View.extend({
    el: '.container',
    template: _.template($('#stock-view-template').html()),

    events: {
        'blur #symbol-field': 'updateStock'
    },

    render: function() {
        this.$('.page').html(this.template(app.Stock.toJSON()));
    },

    updateStock: function() {
        this.render();
    }

});


var appView = new app.AppView();
