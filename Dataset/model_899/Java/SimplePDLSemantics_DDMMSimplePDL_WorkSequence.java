





import java.util.List;
import java.util.ArrayList;

public class SimplePDLSemantics_DDMMSimplePDL_WorkSequence extends ProcessElement {

    private String linkType;



    public SimplePDLSemantics_DDMMSimplePDL_WorkSequence(
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


}