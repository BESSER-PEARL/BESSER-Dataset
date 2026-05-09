





import java.util.List;
import java.util.ArrayList;

public class libraryElement_Identification  {

    private String function;
    private String type;
    private String applicationDomain;
    private String standard;
    private String description;
    private String classification;





    private libraryElement_LibraryElement libraryelement_libraryelement;


    public libraryElement_Identification(
        String function,        String type,        String applicationDomain,        String standard,        String description,        String classification    ) {
        this.function = function;
        this.type = type;
        this.applicationDomain = applicationDomain;
        this.standard = standard;
        this.description = description;
        this.classification = classification;
    }


    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getApplicationdomain() {
        return applicationDomain;
    }

    public void setApplicationdomain(String applicationDomain) {
        this.applicationDomain = applicationDomain;
    }
    public String getStandard() {
        return standard;
    }

    public void setStandard(String standard) {
        this.standard = standard;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getClassification() {
        return classification;
    }

    public void setClassification(String classification) {
        this.classification = classification;
    }

    public libraryElement_LibraryElement getLibraryelement_libraryelement() {
        return libraryelement_libraryelement;
    }

    public void setLibraryelement_libraryelement(libraryElement_LibraryElement libraryelement_libraryelement) {
        this.libraryelement_libraryelement = libraryelement_libraryelement;
    }

}