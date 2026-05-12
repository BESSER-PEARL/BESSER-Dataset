





import java.util.List;
import java.util.ArrayList;

public class sml_Import  {

    private String importURI;





    private sml_Document sml_document;




    private sml_Specification sml_specification;


    public sml_Import(
        String importURI    ) {
        this.importURI = importURI;
    }


    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }

    public sml_Document getSml_document() {
        return sml_document;
    }

    public void setSml_document(sml_Document sml_document) {
        this.sml_document = sml_document;
    }
    public sml_Specification getSml_specification() {
        return sml_specification;
    }

    public void setSml_specification(sml_Specification sml_specification) {
        this.sml_specification = sml_specification;
    }

}