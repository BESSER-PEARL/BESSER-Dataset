





import java.util.List;
import java.util.ArrayList;

public class uma_ProcessPlanningTemplate extends Process {

    private String group4;
    private String baseProcess;



    public uma_ProcessPlanningTemplate(
        String group4,        String baseProcess    ) {
        super(
        );
        this.group4 = group4;
        this.baseProcess = baseProcess;
    }


    public String getGroup4() {
        return group4;
    }

    public void setGroup4(String group4) {
        this.group4 = group4;
    }
    public String getBaseprocess() {
        return baseProcess;
    }

    public void setBaseprocess(String baseProcess) {
        this.baseProcess = baseProcess;
    }


}