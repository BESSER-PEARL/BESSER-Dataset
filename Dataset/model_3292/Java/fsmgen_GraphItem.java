





import java.util.List;
import java.util.ArrayList;

public class fsmgen_GraphItem extends FSMGenElement {

    private boolean inherited;



    public fsmgen_GraphItem(
        boolean inherited    ) {
        super(
        );
        this.inherited = inherited;
    }


    public boolean getInherited() {
        return inherited;
    }

    public void setInherited(boolean inherited) {
        this.inherited = inherited;
    }


}