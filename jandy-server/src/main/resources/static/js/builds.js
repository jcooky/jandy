// Generated by CoffeeScript 1.10.0
(function() {
  var TimelineGraph;

  TimelineGraph = (function() {
    function TimelineGraph() {}

    TimelineGraph.prototype.start = function(projectId) {
      var h, height, paper, w, width;
      h = 140;
      paper = Raphael("timeline", '100%', h);
      height = 110;
      w = $("#timeline").width();
      width = $("#timeline").width() - 10;
      return $.get(ROOT_URL + "/rest/projects/" + projectId + "/builds", (function(_this) {
        return function(builds) {
          var build, duration, dx, i, j, k, l, len, len1, len2, len3, len4, m, mm, n, p, prev, x, y;
          dx = width / (builds.length - 1);
          mm = {
            min: Number.MAX_VALUE,
            max: Number.MIN_VALUE
          };
          for (j = 0, len = builds.length; j < len; j++) {
            build = builds[j];
            if (build.profContextDump.maxTotalDuration < mm.min) {
              mm.min = build.profContextDump.maxTotalDuration;
            }
            if (build.profContextDump.maxTotalDuration > mm.max) {
              mm.max = build.profContextDump.maxTotalDuration;
            }
          }
          i = 0;
          for (k = 0, len1 = builds.length; k < len1; k++) {
            build = builds[k];
            build.num = i++;
          }
          for (l = 0, len2 = builds.length; l < len2; l++) {
            build = builds[l];
            duration = build.profContextDump.maxTotalDuration;
            y = 5 + height - (((duration - mm.min) / (mm.max - mm.min)) * height);
            x = 5 + build.num * dx;
            build.r = {};
            build.r.x = x;
            build.r.y = y;
            build.r.color = build.profContextDump.elapsedDuration <= 0 ? "green" : "red";
            $('.btn btn-primary btn-sm').href;
            console.log($('.btn btn-primary btn-sm').href);
            paper.text(x, h - 5, "#" + build.number).attr('href', "#buildNumber" + build.number);
            paper.path("M" + x + "," + (h - 19) + "L" + x + "," + (h - 11) + "Z");
          }
          prev = null;
          for (m = 0, len3 = builds.length; m < len3; m++) {
            build = builds[m];
            if (prev !== null) {
              p = paper.path("M" + prev.r.x + "," + prev.r.y + "L" + build.r.x + "," + build.r.y + "Z").attr("stroke-width", 2).attr("stroke", "#d3d3d3");
            }
            prev = build;
          }
          for (n = 0, len4 = builds.length; n < len4; n++) {
            build = builds[n];
            paper.circle(build.r.x, build.r.y, 4).attr({
              'fill': build.r.color
            });
          }
          return paper.path("M0," + (h - 15) + "L" + w + "," + (h - 15) + "Z");
        };
      })(this));
    };

    return TimelineGraph;

  })();

  jandy.TimelineGraph = TimelineGraph;

}).call(this);

//# sourceMappingURL=builds.js.map
