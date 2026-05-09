





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ExpansionNode extends ObjectNode {

    private String regionAsOutput;
    private String regionAsInput;



    public UMLModel_ExpansionNode(
        String regionAsOutput,        String regionAsInput    ) {
        super(
        );
        this.regionAsOutput = regionAsOutput;
        this.regionAsInput = regionAsInput;
    }


    public String getRegionasoutput() {
        return regionAsOutput;
    }

    public void setRegionasoutput(String regionAsOutput) {
        this.regionAsOutput = regionAsOutput;
    }
    public String getRegionasinput() {
        return regionAsInput;
    }

    public void setRegionasinput(String regionAsInput) {
        this.regionAsInput = regionAsInput;
    }


}