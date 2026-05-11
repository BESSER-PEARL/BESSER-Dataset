





import java.util.List;
import java.util.ArrayList;

public class base_AllInstancesAccess extends Access {

    private boolean ofKind;



    public base_AllInstancesAccess(
        boolean ofKind    ) {
        super(
        );
        this.ofKind = ofKind;
    }


    public boolean getOfkind() {
        return ofKind;
    }

    public void setOfkind(boolean ofKind) {
        this.ofKind = ofKind;
    }


}