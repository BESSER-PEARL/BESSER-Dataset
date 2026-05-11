





import java.util.List;
import java.util.ArrayList;

public class uml_NamedElement extends Element {

    private String visibility;
    private String name;



    public uml_NamedElement(
        String visibility,        String name    ) {
        super(
        );
        this.visibility = visibility;
        this.name = name;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}