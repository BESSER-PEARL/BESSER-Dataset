





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentTypeRename extends NamedElement {

    private String category;



    public aadl2_ComponentTypeRename(
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


}