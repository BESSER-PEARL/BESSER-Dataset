





import java.util.List;
import java.util.ArrayList;

public class aadl2_FeaturePrototypeReference extends FeaturePrototypeActual {

    private String direction;
    private String in_;
    private String out;





    private aadl2_FeaturePrototype aadl2_featureprototype;


    public aadl2_FeaturePrototypeReference(
        String direction,        String in_,        String out    ) {
        super(
        );
        this.direction = direction;
        this.in_ = in_;
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
    public String getOut() {
        return out;
    }

    public void setOut(String out) {
        this.out = out;
    }

    public aadl2_FeaturePrototype getAadl2_featureprototype() {
        return aadl2_featureprototype;
    }

    public void setAadl2_featureprototype(aadl2_FeaturePrototype aadl2_featureprototype) {
        this.aadl2_featureprototype = aadl2_featureprototype;
    }

}