





import java.util.List;
import java.util.ArrayList;

public class analysis_scheduling_FSMTransition  {

    private String targetStateEnumName;
    private String sourceStateEnumName;



    public analysis_scheduling_FSMTransition(
        String targetStateEnumName,        String sourceStateEnumName    ) {
        this.targetStateEnumName = targetStateEnumName;
        this.sourceStateEnumName = sourceStateEnumName;
    }


    public String getTargetstateenumname() {
        return targetStateEnumName;
    }

    public void setTargetstateenumname(String targetStateEnumName) {
        this.targetStateEnumName = targetStateEnumName;
    }
    public String getSourcestateenumname() {
        return sourceStateEnumName;
    }

    public void setSourcestateenumname(String sourceStateEnumName) {
        this.sourceStateEnumName = sourceStateEnumName;
    }


}