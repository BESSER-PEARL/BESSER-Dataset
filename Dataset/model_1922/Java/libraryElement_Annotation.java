





import java.util.List;
import java.util.ArrayList;

public class libraryElement_Annotation  {

    private String servity;
    private String name;





    private libraryElement_I4DIACElement libraryelement_i4diacelement;


    public libraryElement_Annotation(
        String servity,        String name    ) {
        this.servity = servity;
        this.name = name;
    }


    public String getServity() {
        return servity;
    }

    public void setServity(String servity) {
        this.servity = servity;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public libraryElement_I4DIACElement getLibraryelement_i4diacelement() {
        return libraryelement_i4diacelement;
    }

    public void setLibraryelement_i4diacelement(libraryElement_I4DIACElement libraryelement_i4diacelement) {
        this.libraryelement_i4diacelement = libraryelement_i4diacelement;
    }

}