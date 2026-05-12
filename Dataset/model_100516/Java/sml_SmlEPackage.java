





import java.util.List;
import java.util.ArrayList;

public class sml_SmlEPackage  {

    private String name;





    private sml_Specification sml_specification;




    private sml_Document sml_document;


    public sml_SmlEPackage(
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
    public sml_Document getSml_document() {
        return sml_document;
    }

    public void setSml_document(sml_Document sml_document) {
        this.sml_document = sml_document;
    }

}