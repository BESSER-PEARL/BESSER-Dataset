





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_Feature extends RedefinableElement {

    private boolean static;



    public fUML_Kernel_Feature(
        boolean static    ) {
        super(
        );
        this.static = static;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }


}