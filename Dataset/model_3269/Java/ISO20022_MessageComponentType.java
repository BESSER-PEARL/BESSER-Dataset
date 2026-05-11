





import java.util.List;
import java.util.ArrayList;

public class ISO20022_MessageComponentType extends LogicalType, MessageConcept, TopLevelDictionaryEntry {

    private boolean isTechnical;
    private String tracePath;





    private ISO20022_MessageAttribute iso20022_messageattribute;




    private ISO20022_MessageAssociationEnd iso20022_messageassociationend;


    public ISO20022_MessageComponentType(
        boolean isTechnical,        String tracePath    ) {
        super(
        );
        this.isTechnical = isTechnical;
        this.tracePath = tracePath;
    }


    public boolean getIstechnical() {
        return isTechnical;
    }

    public void setIstechnical(boolean isTechnical) {
        this.isTechnical = isTechnical;
    }
    public String getTracepath() {
        return tracePath;
    }

    public void setTracepath(String tracePath) {
        this.tracePath = tracePath;
    }

    public ISO20022_MessageAttribute getIso20022_messageattribute() {
        return iso20022_messageattribute;
    }

    public void setIso20022_messageattribute(ISO20022_MessageAttribute iso20022_messageattribute) {
        this.iso20022_messageattribute = iso20022_messageattribute;
    }
    public ISO20022_MessageAssociationEnd getIso20022_messageassociationend() {
        return iso20022_messageassociationend;
    }

    public void setIso20022_messageassociationend(ISO20022_MessageAssociationEnd iso20022_messageassociationend) {
        this.iso20022_messageassociationend = iso20022_messageassociationend;
    }

}