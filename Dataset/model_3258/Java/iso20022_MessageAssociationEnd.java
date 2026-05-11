





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageAssociationEnd extends MessageElement {

    private boolean isComposite;



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


}