




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class camel_metric_Schedule  {

    private LocalDate start;
    private int repetitions;
    private String interval;
    private LocalDate end;
    private String name;
    private String type;





    private TimeIntervalUnit timeintervalunit;


    public camel_metric_Schedule(
        LocalDate start,        int repetitions,        String interval,        LocalDate end,        String name,        String type    ) {
        this.start = start;
        this.repetitions = repetitions;
        this.interval = interval;
        this.end = end;
        this.name = name;
        this.type = type;
    }


    public LocalDate getStart() {
        return start;
    }

    public void setStart(LocalDate start) {
        this.start = start;
    }
    public int getRepetitions() {
        return repetitions;
    }

    public void setRepetitions(int repetitions) {
        this.repetitions = repetitions;
    }
    public String getInterval() {
        return interval;
    }

    public void setInterval(String interval) {
        this.interval = interval;
    }
    public LocalDate getEnd() {
        return end;
    }

    public void setEnd(LocalDate end) {
        this.end = end;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public TimeIntervalUnit getTimeintervalunit() {
        return timeintervalunit;
    }

    public void setTimeintervalunit(TimeIntervalUnit timeintervalunit) {
        this.timeintervalunit = timeintervalunit;
    }

}