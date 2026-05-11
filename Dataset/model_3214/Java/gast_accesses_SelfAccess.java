





import java.util.List;
import java.util.ArrayList;

public class gast_accesses_SelfAccess extends VariableAccess {

    private boolean super;



    public gast_accesses_SelfAccess(
        boolean super    ) {
        super(
        );
        this.super = super;
    }


    public boolean getSuper() {
        return super;
    }

    public void setSuper(boolean super) {
        this.super = super;
    }


}