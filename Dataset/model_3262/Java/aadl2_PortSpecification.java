





import java.util.List;
import java.util.ArrayList;

public class aadl2_PortSpecification extends FeaturePrototypeActual {

    private String category;
    private String direction;





    private aadl2_ComponentPrototype aadl2_componentprototype;




    private aadl2_ComponentClassifier aadl2_componentclassifier;


    public aadl2_PortSpecification(
        String category,        String direction    ) {
        super(
        );
        this.category = category;
        this.direction = direction;
    }


    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
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