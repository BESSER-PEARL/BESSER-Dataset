





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentPrototypeActual extends ArrayableElement {

    private String category;





    private aadl2_ComponentPrototypeBinding aadl2_componentprototypebinding;


    public aadl2_ComponentPrototypeActual(
        String category    ) {
        super(
        );
        this.category = category;
    }


    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public aadl2_ComponentPrototypeBinding getAadl2_componentprototypebinding() {
        return aadl2_componentprototypebinding;
    }

    public void setAadl2_componentprototypebinding(aadl2_ComponentPrototypeBinding aadl2_componentprototypebinding) {
        this.aadl2_componentprototypebinding = aadl2_componentprototypebinding;
    }

}