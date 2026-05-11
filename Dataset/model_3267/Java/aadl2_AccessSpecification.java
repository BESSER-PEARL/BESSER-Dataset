





import java.util.List;
import java.util.ArrayList;

public class aadl2_AccessSpecification extends FeaturePrototypeActual {

    private String category;
    private String kind;





    private aadl2_ComponentPrototype aadl2_componentprototype;


    public aadl2_AccessSpecification(
        String category,        String kind    ) {
        super(
        );
        this.category = category;
        this.kind = kind;
    }


    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public aadl2_ComponentPrototype getAadl2_componentprototype() {
        return aadl2_componentprototype;
    }

    public void setAadl2_componentprototype(aadl2_ComponentPrototype aadl2_componentprototype) {
        this.aadl2_componentprototype = aadl2_componentprototype;
    }

}