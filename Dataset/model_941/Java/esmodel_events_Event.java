




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_events_Event  {

    private LocalDate timestamp;



    public esmodel_events_Event(
        LocalDate timestamp    ) {
        this.timestamp = timestamp;
    }


    public LocalDate getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDate timestamp) {
        this.timestamp = timestamp;
    }


}