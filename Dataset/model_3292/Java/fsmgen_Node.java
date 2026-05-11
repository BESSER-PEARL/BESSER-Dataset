





import java.util.List;
import java.util.ArrayList;

public class fsmgen_Node extends GraphItem {

    private int inheritanceLevel;



    public fsmgen_Node(
        int inheritanceLevel    ) {
        super(
        );
        this.inheritanceLevel = inheritanceLevel;
    }


    public int getInheritancelevel() {
        return inheritanceLevel;
    }

    public void setInheritancelevel(int inheritanceLevel) {
        this.inheritanceLevel = inheritanceLevel;
    }


}