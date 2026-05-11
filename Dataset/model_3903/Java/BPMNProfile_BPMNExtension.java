





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BPMNExtension  {

    private String mustUnderstand;





    private BPMNProfile_ExtensionDefinition bpmnprofile_extensiondefinition;




    private BPMNProfile_Definitions bpmnprofile_definitions;




    private BPMNProfile_Stereotype bpmnprofile_stereotype;


    public BPMNProfile_BPMNExtension(
        String mustUnderstand    ) {
        this.mustUnderstand = mustUnderstand;
    }


    public String getMustunderstand() {
        return mustUnderstand;
    }

    public void setMustunderstand(String mustUnderstand) {
        this.mustUnderstand = mustUnderstand;
    }

    public BPMNProfile_ExtensionDefinition getBpmnprofile_extensiondefinition() {
        return bpmnprofile_extensiondefinition;
    }

    public void setBpmnprofile_extensiondefinition(BPMNProfile_ExtensionDefinition bpmnprofile_extensiondefinition) {
        this.bpmnprofile_extensiondefinition = bpmnprofile_extensiondefinition;
    }
    public BPMNProfile_Definitions getBpmnprofile_definitions() {
        return bpmnprofile_definitions;
    }

    public void setBpmnprofile_definitions(BPMNProfile_Definitions bpmnprofile_definitions) {
        this.bpmnprofile_definitions = bpmnprofile_definitions;
    }
    public BPMNProfile_Stereotype getBpmnprofile_stereotype() {
        return bpmnprofile_stereotype;
    }

    public void setBpmnprofile_stereotype(BPMNProfile_Stereotype bpmnprofile_stereotype) {
        this.bpmnprofile_stereotype = bpmnprofile_stereotype;
    }

}