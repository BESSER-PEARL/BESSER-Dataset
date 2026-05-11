





import java.util.List;
import java.util.ArrayList;

public class modelDsl_Package extends Element {






    private List<modelDsl_Element> modeldsl_elements;


    public modelDsl_Package(
    ) {
        super(
        );
        this.modeldsl_elements = new ArrayList<>();
    }

    public modelDsl_Package(
        ArrayList<modelDsl_Element> modeldsl_elements    ) {
        this.modeldsl_elements = modeldsl_elements;
    }


    public List<modelDsl_Element> getModeldsl_elements() {
        return modeldsl_elements;
    }

    public void addModeldsl_element(Modeldsl_element modeldsl_element) {
        this.modeldsl_elements.add(modeldsl_element);
    }

}