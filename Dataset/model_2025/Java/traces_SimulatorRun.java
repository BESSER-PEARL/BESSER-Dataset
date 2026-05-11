




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class traces_SimulatorRun  {

    private String behaviorName;
    private LocalDate timestamp;
    private int id;



    public traces_SimulatorRun(
        String behaviorName,        LocalDate timestamp,        int id    ) {
        this.behaviorName = behaviorName;
        this.timestamp = timestamp;
        this.id = id;
    }


    public String getBehaviorname() {
        return behaviorName;
    }

    public void setBehaviorname(String behaviorName) {
        this.behaviorName = behaviorName;
    }
    public LocalDate getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDate timestamp) {
        this.timestamp = timestamp;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}