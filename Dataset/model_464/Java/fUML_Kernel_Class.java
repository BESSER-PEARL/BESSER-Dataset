





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_Class extends BehavioredClassifier {

    private boolean active;



    public fUML_Kernel_Class(
        boolean active    ) {
        super(
        );
        this.active = active;
    }


    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }


}