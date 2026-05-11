





import java.util.List;
import java.util.ArrayList;

public class classes_Attribute extends NamedElement, TypedElement {

    private boolean isMany;



    public classes_Attribute(
        boolean isMany    ) {
        super(
        );
        this.isMany = isMany;
    }


    public boolean getIsmany() {
        return isMany;
    }

    public void setIsmany(boolean isMany) {
        this.isMany = isMany;
    }


}