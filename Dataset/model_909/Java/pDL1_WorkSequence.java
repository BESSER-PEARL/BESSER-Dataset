





import java.util.List;
import java.util.ArrayList;

public class pDL1_WorkSequence extends ProcessElement {

    private String linkType;





    private pDL1_WorkDefinition pdl1_workdefinition;




    private pDL1_WorkDefinition pdl1_workdefinition;


    public pDL1_WorkSequence(
        String linkType    ) {
        super(
        );
        this.linkType = linkType;
    }


    public String getLinktype() {
        return linkType;
    }

    public void setLinktype(String linkType) {
        this.linkType = linkType;
    }

    public pDL1_WorkDefinition getPdl1_workdefinition() {
        return pdl1_workdefinition;
    }

    public void setPdl1_workdefinition(pDL1_WorkDefinition pdl1_workdefinition) {
        this.pdl1_workdefinition = pdl1_workdefinition;
    }
    public pDL1_WorkDefinition getPdl1_workdefinition() {
        return pdl1_workdefinition;
    }

    public void setPdl1_workdefinition(pDL1_WorkDefinition pdl1_workdefinition) {
        this.pdl1_workdefinition = pdl1_workdefinition;
    }

}