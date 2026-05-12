





import java.util.List;
import java.util.ArrayList;

public class sml_SmlETypedElement  {

    private String name;





    private sml_Specification sml_specification;


    public sml_SmlETypedElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sml_Specification getSml_specification() {
        return sml_specification;
    }

    public void setSml_specification(sml_Specification sml_specification) {
        this.sml_specification = sml_specification;
    }

}