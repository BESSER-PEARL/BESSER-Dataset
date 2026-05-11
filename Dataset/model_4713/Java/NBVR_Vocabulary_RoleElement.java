





import java.util.List;
import java.util.ArrayList;

public class NBVR_Vocabulary_RoleElement extends FormElement {

    private int slot;





    private VerbRole verbrole;


    public NBVR_Vocabulary_RoleElement(
        int slot    ) {
        super(
        );
        this.slot = slot;
    }


    public int getSlot() {
        return slot;
    }

    public void setSlot(int slot) {
        this.slot = slot;
    }

    public VerbRole getVerbrole() {
        return verbrole;
    }

    public void setVerbrole(VerbRole verbrole) {
        this.verbrole = verbrole;
    }

}