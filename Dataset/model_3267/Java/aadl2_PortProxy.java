





import java.util.List;
import java.util.ArrayList;

public class aadl2_PortProxy extends ProcessorFeature, TriggerPort, PortConnectionEnd, FeatureConnectionEnd {

    private String out;
    private String in_;
    private String direction;



    public aadl2_PortProxy(
        String out,        String in_,        String direction    ) {
        super(
        );
        this.out = out;
        this.in_ = in_;
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
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }


}