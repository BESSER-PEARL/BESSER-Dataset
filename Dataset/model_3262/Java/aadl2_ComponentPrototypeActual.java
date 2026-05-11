





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentPrototypeActual extends ArrayableElement {

    private String category;





    private aadl2_SubcomponentType aadl2_subcomponenttype;


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

    public aadl2_SubcomponentType getAadl2_subcomponenttype() {
        return aadl2_subcomponenttype;
    }

    public void setAadl2_subcomponenttype(aadl2_SubcomponentType aadl2_subcomponenttype) {
        this.aadl2_subcomponenttype = aadl2_subcomponenttype;
    }

}