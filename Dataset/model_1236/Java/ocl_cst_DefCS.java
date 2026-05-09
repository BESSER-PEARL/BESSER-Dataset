





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_DefCS extends InvOrDefCS {

    private boolean static;



    public ocl_cst_DefCS(
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