





import java.util.List;
import java.util.ArrayList;

public class aadl2_DirectedFeature extends Feature {

    private String out;
    private String direction;
    private String in_;



    public aadl2_DirectedFeature(
        String out,        String direction,        String in_    ) {
        super(
        );
        this.out = out;
        this.direction = direction;
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
    public String getIn_() {
        return in_;
    }

    public void setIn_(String in_) {
        this.in_ = in_;
    }


}