





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_BPMNExtension  {

    private String mustUnderstand;





    private bpmnprof_Definitions bpmnprof_definitions;




    private bpmnprof_ExtensionDefinition bpmnprof_extensiondefinition;




    private bpmnprof_Stereotype bpmnprof_stereotype;


    public bpmnprof_BPMNExtension(
        String mustUnderstand    ) {
        this.mustUnderstand = mustUnderstand;
    }


    public String getMustunderstand() {
        return mustUnderstand;
    }

    public void setMustunderstand(String mustUnderstand) {
        this.mustUnderstand = mustUnderstand;
    }

    public bpmnprof_Definitions getBpmnprof_definitions() {
        return bpmnprof_definitions;
    }

    public void setBpmnprof_definitions(bpmnprof_Definitions bpmnprof_definitions) {
        this.bpmnprof_definitions = bpmnprof_definitions;
    }
    public bpmnprof_ExtensionDefinition getBpmnprof_extensiondefinition() {
        return bpmnprof_extensiondefinition;
    }

    public void setBpmnprof_extensiondefinition(bpmnprof_ExtensionDefinition bpmnprof_extensiondefinition) {
        this.bpmnprof_extensiondefinition = bpmnprof_extensiondefinition;
    }
    public bpmnprof_Stereotype getBpmnprof_stereotype() {
        return bpmnprof_stereotype;
    }

    public void setBpmnprof_stereotype(bpmnprof_Stereotype bpmnprof_stereotype) {
        this.bpmnprof_stereotype = bpmnprof_stereotype;
    }

}