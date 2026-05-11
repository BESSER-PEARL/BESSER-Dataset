





import java.util.List;
import java.util.ArrayList;

public class uml_NamedElement extends Element {

    private String name;
    private String visibility;



    public uml_NamedElement(
        String name,        String visibility    ) {
        super(
        );
        this.name = name;
        this.visibility = visibility;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }


}