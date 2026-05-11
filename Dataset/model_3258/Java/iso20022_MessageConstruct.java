





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageConstruct extends Construct {

    private String xmlTag;





    private iso20022_LogicalType iso20022_logicaltype;


    public iso20022_MessageConstruct(
        String xmlTag    ) {
        super(
        );
        this.xmlTag = xmlTag;
    }


    public String getXmltag() {
        return xmlTag;
    }

    public void setXmltag(String xmlTag) {
        this.xmlTag = xmlTag;
    }

    public iso20022_LogicalType getIso20022_logicaltype() {
        return iso20022_logicaltype;
    }

    public void setIso20022_logicaltype(iso20022_LogicalType iso20022_logicaltype) {
        this.iso20022_logicaltype = iso20022_logicaltype;
    }

}