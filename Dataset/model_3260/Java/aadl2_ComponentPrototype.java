





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentPrototype extends Prototype {

    private String array;
    private String category;





    private aadl2_ComponentClassifier aadl2_componentclassifier;




    private aadl2_Subcomponent aadl2_subcomponent;




    private aadl2_ComponentPrototypeReference aadl2_componentprototypereference;


    public aadl2_ComponentPrototype(
        String array,        String category    ) {
        super(
        );
        this.array = array;
        this.category = category;
    }


    public String getArray() {
        return array;
    }

    public void setArray(String array) {
        this.array = array;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public aadl2_ComponentClassifier getAadl2_componentclassifier() {
        return aadl2_componentclassifier;
    }

    public void setAadl2_componentclassifier(aadl2_ComponentClassifier aadl2_componentclassifier) {
        this.aadl2_componentclassifier = aadl2_componentclassifier;
    }
    public aadl2_Subcomponent getAadl2_subcomponent() {
        return aadl2_subcomponent;
    }

    public void setAadl2_subcomponent(aadl2_Subcomponent aadl2_subcomponent) {
        this.aadl2_subcomponent = aadl2_subcomponent;
    }
    public aadl2_ComponentPrototypeReference getAadl2_componentprototypereference() {
        return aadl2_componentprototypereference;
    }

    public void setAadl2_componentprototypereference(aadl2_ComponentPrototypeReference aadl2_componentprototypereference) {
        this.aadl2_componentprototypereference = aadl2_componentprototypereference;
    }

}