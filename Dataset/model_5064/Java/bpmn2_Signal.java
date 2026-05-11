





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Signal extends RootElement {






    private bpmn2_ItemDefinition bpmn2_itemdefinition;




    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_SignalEventDefinition bpmn2_signaleventdefinition;


    public bpmn2_Signal(
    ) {
        super(
        );
    }



    public bpmn2_ItemDefinition getBpmn2_itemdefinition() {
        return bpmn2_itemdefinition;
    }

    public void setBpmn2_itemdefinition(bpmn2_ItemDefinition bpmn2_itemdefinition) {
        this.bpmn2_itemdefinition = bpmn2_itemdefinition;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_SignalEventDefinition getBpmn2_signaleventdefinition() {
        return bpmn2_signaleventdefinition;
    }

    public void setBpmn2_signaleventdefinition(bpmn2_SignalEventDefinition bpmn2_signaleventdefinition) {
        this.bpmn2_signaleventdefinition = bpmn2_signaleventdefinition;
    }

}