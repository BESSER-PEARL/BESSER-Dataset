





import java.util.List;
import java.util.ArrayList;

public class aadl2_FeaturePrototype extends Prototype {

    private String in_;
    private String direction;
    private String out;





    private aadl2_AbstractFeature aadl2_abstractfeature;




    private aadl2_ComponentClassifier aadl2_componentclassifier;


    public aadl2_FeaturePrototype(
        String in_,        String direction,        String out    ) {
        super(
        );
        this.in_ = in_;
        this.direction = direction;
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
    public String getOut() {
        return out;
    }

    public void setOut(String out) {
        this.out = out;
    }

    public aadl2_AbstractFeature getAadl2_abstractfeature() {
        return aadl2_abstractfeature;
    }

    public void setAadl2_abstractfeature(aadl2_AbstractFeature aadl2_abstractfeature) {
        this.aadl2_abstractfeature = aadl2_abstractfeature;
    }
    public aadl2_ComponentClassifier getAadl2_componentclassifier() {
        return aadl2_componentclassifier;
    }

    public void setAadl2_componentclassifier(aadl2_ComponentClassifier aadl2_componentclassifier) {
        this.aadl2_componentclassifier = aadl2_componentclassifier;
    }

}