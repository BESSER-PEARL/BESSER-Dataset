





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Interface extends RootElement {

    private String name;





    private bpmn2_CallableElement bpmn2_callableelement;


    public bpmn2_Interface(
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

    public bpmn2_CallableElement getBpmn2_callableelement() {
        return bpmn2_callableelement;
    }

    public void setBpmn2_callableelement(bpmn2_CallableElement bpmn2_callableelement) {
        this.bpmn2_callableelement = bpmn2_callableelement;
    }

}