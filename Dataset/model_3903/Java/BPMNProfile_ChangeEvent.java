





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ChangeEvent  {






    private BPMNProfile_ConditionalEventDefinition bpmnprofile_conditionaleventdefinition;




    private BPMNProfile_TimerEventDefinition bpmnprofile_timereventdefinition;


    public BPMNProfile_ChangeEvent(
    ) {
    }



    public BPMNProfile_ConditionalEventDefinition getBpmnprofile_conditionaleventdefinition() {
        return bpmnprofile_conditionaleventdefinition;
    }

    public void setBpmnprofile_conditionaleventdefinition(BPMNProfile_ConditionalEventDefinition bpmnprofile_conditionaleventdefinition) {
        this.bpmnprofile_conditionaleventdefinition = bpmnprofile_conditionaleventdefinition;
    }
    public BPMNProfile_TimerEventDefinition getBpmnprofile_timereventdefinition() {
        return bpmnprofile_timereventdefinition;
    }

    public void setBpmnprofile_timereventdefinition(BPMNProfile_TimerEventDefinition bpmnprofile_timereventdefinition) {
        this.bpmnprofile_timereventdefinition = bpmnprofile_timereventdefinition;
    }

}