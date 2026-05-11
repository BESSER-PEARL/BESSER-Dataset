





import java.util.List;
import java.util.ArrayList;

public class aadl2_InternalFeature extends TriggerPort, PortConnectionEnd, StructuralFeature, FeatureConnectionEnd {

    private String in_;
    private String out;
    private String direction;



    public aadl2_InternalFeature(
        String in_,        String out,        String direction    ) {
        super(
        );
        this.in_ = in_;
        this.out = out;
        this.direction = direction;
    }


    public String getIn_() {
        return in_;
    }

    public void setIn_(String in_) {
        this.in_ = in_;
    }
    public String getOut() {
        return out;
    }

    public void setOut(String out) {
        this.out = out;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }


}