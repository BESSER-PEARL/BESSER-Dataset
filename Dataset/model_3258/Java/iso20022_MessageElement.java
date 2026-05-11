





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageElement extends MessageConcept, MessageConstruct {

    private boolean isDerived;
    private boolean isTechnical;





    private iso20022_Xor iso20022_xor;


    public iso20022_MessageElement(
        boolean isDerived,        boolean isTechnical    ) {
        super(
        );
        this.isDerived = isDerived;
        this.isTechnical = isTechnical;
    }


    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }
    public boolean getIstechnical() {
        return isTechnical;
    }

    public void setIstechnical(boolean isTechnical) {
        this.isTechnical = isTechnical;
    }

    public iso20022_Xor getIso20022_xor() {
        return iso20022_xor;
    }

    public void setIso20022_xor(iso20022_Xor iso20022_xor) {
        this.iso20022_xor = iso20022_xor;
    }

}