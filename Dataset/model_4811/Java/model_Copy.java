





import java.util.List;
import java.util.ArrayList;

public class model_Copy extends BPELExtensibleElement {

    private String keepSrcElementName;
    private String ignoreMissingFromData;



    public model_Copy(
        String keepSrcElementName,        String ignoreMissingFromData    ) {
        super(
        );
        this.keepSrcElementName = keepSrcElementName;
        this.ignoreMissingFromData = ignoreMissingFromData;
    }


    public String getKeepsrcelementname() {
        return keepSrcElementName;
    }

    public void setKeepsrcelementname(String keepSrcElementName) {
        this.keepSrcElementName = keepSrcElementName;
    }
    public String getIgnoremissingfromdata() {
        return ignoreMissingFromData;
    }

    public void setIgnoremissingfromdata(String ignoreMissingFromData) {
        this.ignoreMissingFromData = ignoreMissingFromData;
    }


}