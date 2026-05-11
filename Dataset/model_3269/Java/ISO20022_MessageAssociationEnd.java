





import java.util.List;
import java.util.ArrayList;

public class ISO20022_MessageAssociationEnd extends MessageElement {

    private boolean isComposite;





    private ISO20022_MessageAssociationEnd iso20022_messageassociationend;


    public ISO20022_MessageAssociationEnd(
        boolean isComposite    ) {
        super(
        );
        this.isComposite = isComposite;
    }


    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }

    public ISO20022_MessageAssociationEnd getIso20022_messageassociationend() {
        return iso20022_messageassociationend;
    }

    public void setIso20022_messageassociationend(ISO20022_MessageAssociationEnd iso20022_messageassociationend) {
        this.iso20022_messageassociationend = iso20022_messageassociationend;
    }

}