





import java.util.List;
import java.util.ArrayList;

public class frontend_core_OptimizationsAnnotation extends Annotation {

    private boolean enabled;



    public frontend_core_OptimizationsAnnotation(
        boolean enabled    ) {
        super(
        );
        this.enabled = enabled;
    }


    public boolean getEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }


}