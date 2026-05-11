





import java.util.List;
import java.util.ArrayList;

public class aadl2_InternalFeature extends TriggerPort, StructuralFeature, PortConnectionEnd, FeatureConnectionEnd {

    private String direction;
    private String out;
    private String in_;



    public aadl2_InternalFeature(
        String direction,        String out,        String in_    ) {
        super(
        );
        this.direction = direction;
        this.out = out;
        this.in_ = in_;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getOut() {
        return out;
    }

    public void setOut(String out) {
        this.out = out;
    }
    public String getIn_() {
        return in_;
    }

    public void setIn_(String in_) {
        this.in_ = in_;
    }


}