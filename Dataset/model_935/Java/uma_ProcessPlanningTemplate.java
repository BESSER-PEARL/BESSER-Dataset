





import java.util.List;
import java.util.ArrayList;

public class uma_ProcessPlanningTemplate extends Process {

    private String baseProcess;
    private String group4;



    public uma_ProcessPlanningTemplate(
        String baseProcess,        String group4    ) {
        super(
        );
        this.baseProcess = baseProcess;
        this.group4 = group4;
    }


    public String getBaseprocess() {
        return baseProcess;
    }

    public void setBaseprocess(String baseProcess) {
        this.baseProcess = baseProcess;
    }
    public String getGroup4() {
        return group4;
    }

    public void setGroup4(String group4) {
        this.group4 = group4;
    }


}