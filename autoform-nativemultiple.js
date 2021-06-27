AutoForm.addInputType("nativemultiple", {
  template: "afNativeMultiple",
  valueOut: function () {
    return this.attr('value');
  },
  // valueConverters: {
  //   // "number": AutoForm.Utility.stringToNumber,
  //   "numberArray": function (val) {
  //     if (_.isArray(val)) {
  //       return _.map(val, function (item) {
  //         item = $.trim(item);
  //         return AutoForm.Utility.stringToNumber(item);
  //       });
  //     }
  //     return val;
  //   }
  // }
});

Template.afNativeMultiple.helpers({
  atts: function () {
    var atts = _.clone(this.atts);
    delete atts.nativeMultipleOptions;
    return atts;
  }
});

Template.afNativeMultiple.rendered = function () {
  // instanciate nativemultiple
  this.$('input[type="range"]').nativeMultiple(this.data.atts.nativeMultipleOptions || {});
};
