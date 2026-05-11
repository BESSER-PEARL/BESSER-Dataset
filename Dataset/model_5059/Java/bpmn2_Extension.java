





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Extension  {

    private boolean mustUnderstand;
    private String id;





    private bpmn2_Definitions bpmn2_definitions;




    private bpmn2_ExtensionDefinition bpmn2_extensiondefinition;


    public bpmn2_Extension(
        boolean mustUnderstand,        String id    ) {
        this.mustUnderstand = mustUnderstand;
        this.id = id;
    }


    public boolean getMustunderstand() {
        return mustUnderstand;
    }

    public void setMustunderstand(boolean mustUnderstand) {
        this.mustUnderstand = mustUnderstand;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public bpmn2_Definitions getBpmn2_definitions() {
        return bpmn2_definitions;
    }

    public void setBpmn2_definitions(bpmn2_Definitions bpmn2_definitions) {
        this.bpmn2_definitions = bpmn2_definitions;
    }
    public bpmn2_ExtensionDefinition getBpmn2_extensiondefinition() {
        return bpmn2_extensiondefinition;
    }

    public void setBpmn2_extensiondefinition(bpmn2_ExtensionDefinition bpmn2_extensiondefinition) {
        this.bpmn2_extensiondefinition = bpmn2_extensiondefinition;
    }

}