





import java.util.List;
import java.util.ArrayList;

public class aadl2_AccessSpecification extends FeaturePrototypeActual {

    private String kind;
    private String category;





    private aadl2_ComponentPrototype aadl2_componentprototype;




    private aadl2_ComponentClassifier aadl2_componentclassifier;


    public aadl2_AccessSpecification(
        String kind,        String category    ) {
        super(
        );
        this.kind = kind;
        this.category = category;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
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