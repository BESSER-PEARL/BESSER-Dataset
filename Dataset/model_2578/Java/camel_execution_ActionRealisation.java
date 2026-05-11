




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class camel_execution_ActionRealisation  {

    private LocalDate endTime;
    private String name;
    private String lowLevelActions;
    private LocalDate startTime;



    public camel_execution_ActionRealisation(
        LocalDate endTime,        String name,        String lowLevelActions,        LocalDate startTime    ) {
        this.endTime = endTime;
        this.name = name;
        this.lowLevelActions = lowLevelActions;
        this.startTime = startTime;
    }


    public LocalDate getEndtime() {
        return endTime;
    }

    public void setEndtime(LocalDate endTime) {
        this.endTime = endTime;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLowlevelactions() {
        return lowLevelActions;
    }

    public void setLowlevelactions(String lowLevelActions) {
        this.lowLevelActions = lowLevelActions;
    }
    public LocalDate getStarttime() {
        return startTime;
    }

    public void setStarttime(LocalDate startTime) {
        this.startTime = startTime;
    }


}