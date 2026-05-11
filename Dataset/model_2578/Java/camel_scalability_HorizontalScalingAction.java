





import java.util.List;
import java.util.ArrayList;

public class camel_scalability_HorizontalScalingAction extends ScalingAction {

    private int count;





    private InternalComponent internalcomponent;


    public camel_scalability_HorizontalScalingAction(
        int count    ) {
        super(
        );
        this.count = count;
    }


    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public InternalComponent getInternalcomponent() {
        return internalcomponent;
    }

    public void setInternalcomponent(InternalComponent internalcomponent) {
        this.internalcomponent = internalcomponent;
    }

}