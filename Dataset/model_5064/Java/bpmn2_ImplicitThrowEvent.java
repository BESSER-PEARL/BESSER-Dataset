





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ImplicitThrowEvent extends ThrowEvent {






    private bpmn2_ComplexBehaviorDefinition bpmn2_complexbehaviordefinition;




    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_ImplicitThrowEvent(
    ) {
        super(
        );
    }



    public bpmn2_ComplexBehaviorDefinition getBpmn2_complexbehaviordefinition() {
        return bpmn2_complexbehaviordefinition;
    }

    public void setBpmn2_complexbehaviordefinition(bpmn2_ComplexBehaviorDefinition bpmn2_complexbehaviordefinition) {
        this.bpmn2_complexbehaviordefinition = bpmn2_complexbehaviordefinition;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}