





import java.util.List;
import java.util.ArrayList;

public class camel_requirement_HorizontalScaleRequirement extends ScaleRequirement {

    private int minInstances;
    private int maxInstances;





    private InternalComponent internalcomponent;


    public camel_requirement_HorizontalScaleRequirement(
        int minInstances,        int maxInstances    ) {
        super(
        );
        this.minInstances = minInstances;
        this.maxInstances = maxInstances;
    }


    public int getMininstances() {
        return minInstances;
    }

    public void setMininstances(int minInstances) {
        this.minInstances = minInstances;
    }
    public int getMaxinstances() {
        return maxInstances;
    }

    public void setMaxinstances(int maxInstances) {
        this.maxInstances = maxInstances;
    }

    public InternalComponent getInternalcomponent() {
        return internalcomponent;
    }

    public void setInternalcomponent(InternalComponent internalcomponent) {
        this.internalcomponent = internalcomponent;
    }

}