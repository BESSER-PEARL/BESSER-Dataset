





import java.util.List;
import java.util.ArrayList;

public class ecore_ENamedElement extends EModelElement {

    private String name;



    public ecore_ENamedElement(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}