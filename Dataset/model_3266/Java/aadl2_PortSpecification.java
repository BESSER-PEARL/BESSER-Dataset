





import java.util.List;
import java.util.ArrayList;

public class aadl2_PortSpecification extends FeaturePrototypeActual {

    private String direction;
    private String category;
    private String out;
    private String in_;





    private aadl2_ComponentPrototype aadl2_componentprototype;




    private aadl2_ComponentClassifier aadl2_componentclassifier;


    public aadl2_PortSpecification(
        String direction,        String category,        String out,        String in_    ) {
        super(
        );
        this.direction = direction;
        this.category = category;
        this.out = out;
        this.in_ = in_;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
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

    public aadl2_ComponentPrototype getAadl2_componentprototype() {
        return aadl2_componentprototype;
    }

    public void setAadl2_componentprototype(aadl2_ComponentPrototype aadl2_componentprototype) {
        this.aadl2_componentprototype = aadl2_componentprototype;
    }
    public aadl2_ComponentClassifier getAadl2_componentclassifier() {
        return aadl2_componentclassifier;
    }

    public void setAadl2_componentclassifier(aadl2_ComponentClassifier aadl2_componentclassifier) {
        this.aadl2_componentclassifier = aadl2_componentclassifier;
    }

}