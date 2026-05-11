





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BPMNExtension  {

    private String mustUnderstand;





    private BPMNProfile_Definitions bpmnprofile_definitions;


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

    public BPMNProfile_Definitions getBpmnprofile_definitions() {
        return bpmnprofile_definitions;
    }

    public void setBpmnprofile_definitions(BPMNProfile_Definitions bpmnprofile_definitions) {
        this.bpmnprofile_definitions = bpmnprofile_definitions;
    }

}