





import java.util.List;
import java.util.ArrayList;

public class gast_core_NamedModelElement extends ModelElement {

    private String simpleName;



    public gast_core_NamedModelElement(
        String simpleName    ) {
        super(
        );
        this.simpleName = simpleName;
    }


    public String getSimplename() {
        return simpleName;
    }

    public void setSimplename(String simpleName) {
        this.simpleName = simpleName;
    }


}