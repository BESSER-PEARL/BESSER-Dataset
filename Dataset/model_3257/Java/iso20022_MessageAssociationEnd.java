





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageAssociationEnd extends MessageElement {

    private boolean isComposite;





    private iso20022_MessageComponentType iso20022_messagecomponenttype;


    public iso20022_MessageAssociationEnd(
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

    public iso20022_MessageComponentType getIso20022_messagecomponenttype() {
        return iso20022_messagecomponenttype;
    }

    public void setIso20022_messagecomponenttype(iso20022_MessageComponentType iso20022_messagecomponenttype) {
        this.iso20022_messagecomponenttype = iso20022_messagecomponenttype;
    }

}