





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ExtensionDefinition  {

    private String name;
    private String id;





    private bpmn2_BaseElement bpmn2_baseelement;


    public bpmn2_ExtensionDefinition(
        String name,        String id    ) {
        this.name = name;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public bpmn2_BaseElement getBpmn2_baseelement() {
        return bpmn2_baseelement;
    }

    public void setBpmn2_baseelement(bpmn2_BaseElement bpmn2_baseelement) {
        this.bpmn2_baseelement = bpmn2_baseelement;
    }

}