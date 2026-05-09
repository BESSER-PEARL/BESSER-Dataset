





import java.util.List;
import java.util.ArrayList;

public class family_Members extends NamedElement {

    private boolean hasChild;



    public family_Members(
        boolean hasChild    ) {
        super(
        );
        this.hasChild = hasChild;
    }


    public boolean getHaschild() {
        return hasChild;
    }

    public void setHaschild(boolean hasChild) {
        this.hasChild = hasChild;
    }


}