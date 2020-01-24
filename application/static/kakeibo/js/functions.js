$(function() {
    //  dropdown on the menu
    $('.ui.dropdown').dropdown({ on: 'hover' });
    // fade out message
    setTimeout(function() {
      $('.js-fade-message').transition('fade up', '2000ms');
    }, 2000);
    // show the category modal
    $("#category-modal").click(function(){
      $(".ui.category.modal").modal('show');
    });
    // delete expense modal
    $("[class*=delete-expense-]").click(function(){
      // generate delete path
      var pk = $(this, ".delete.button").attr('class').match(/\d+/)[0];
      $(".delete-expense-modal").attr("action", "/kakeibo_management/delete_expense/" + pk + "/");
      $('.delete-expense-modal').modal('show');
    });
    // delete earning modal
    $("[class*=delete-earning-]").click(function(){
      // generate delete path
      var pk = $(this, ".delete.button").attr('class').match(/\d+/)[0];
      $(".delete-earning-modal").attr("action", "/kakeibo_management/delete_earning/" + pk + "/");
      $('.delete-earning-modal').modal('show');
    });
    // calendar in the forms
    $("#expense-modal").click(function(){
      $(".expense.modal").modal({
        onShow: function(){
          $('.ui.calendar').calendar({
            type: 'date',formatter: {
              date: function(date, settings){
                if(!date) return '';
                var day = ("0" + date.getDate()).slice(-2);
                var month = ("0" + (date.getMonth() + 1)).slice(-2);
                var year = date.getFullYear();
                return year + '-' + month + '-' + day;
              }
            }
          });
        }
      }).modal('show');
    });

    $("#earning-modal").click(function(){
      $(".earning.modal").modal({
        onShow: function(){
          $('.ui.calendar').calendar({
            type: 'date',formatter: {
              date: function(date, settings){
                if(!date) return '';
                var day = ("0" + date.getDate()).slice(-2);
                var month = ("0" + (date.getMonth() + 1)).slice(-2);
                var year = date.getFullYear();
                return year + '-' + month + '-' + day;
              }
            }
          });
        }
      }).modal('show');
    });
    // expense calendar in the edit
    $('#calendar').calendar({
      type: 'date',formatter: {
        date: function(date, settings){
          if(!date) return '';
          var day = ("0" + date.getDate()).slice(-2);
          var month = ("0" + (date.getMonth() + 1)).slice(-2);
          var year = date.getFullYear();
          return year + '-' + month + '-' + day;
        }
      }
    });
  });