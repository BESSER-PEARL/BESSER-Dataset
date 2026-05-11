





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Signal extends RootElement {

    private String name;





    private bpmn2_SignalEventDefinition bpmn2_signaleventdefinition;


    public bpmn2_Signal(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_SignalEventDefinition getBpmn2_signaleventdefinition() {
        return bpmn2_signaleventdefinition;
    }

    public void setBpmn2_signaleventdefinition(bpmn2_SignalEventDefinition bpmn2_signaleventdefinition) {
        this.bpmn2_signaleventdefinition = bpmn2_signaleventdefinition;
    }

}