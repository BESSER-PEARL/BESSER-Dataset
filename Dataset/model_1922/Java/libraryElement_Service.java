





import java.util.List;
import java.util.ArrayList;

public class libraryElement_Service extends I4DIACElement {






    private libraryElement_FBType libraryelement_fbtype;




    private List<libraryElement_ServiceSequence> libraryelement_servicesequences;




    private libraryElement_ServiceInterface libraryelement_serviceinterface;




    private libraryElement_ServiceInterface libraryelement_serviceinterface;


    public libraryElement_Service(
    ) {
        super(
        );
        this.libraryelement_servicesequences = new ArrayList<>();
    }

    public libraryElement_Service(
        ArrayList<libraryElement_ServiceSequence> libraryelement_servicesequences    ) {
        this.libraryelement_servicesequences = libraryelement_servicesequences;
    }


    public libraryElement_FBType getLibraryelement_fbtype() {
        return libraryelement_fbtype;
    }

    public void setLibraryelement_fbtype(libraryElement_FBType libraryelement_fbtype) {
        this.libraryelement_fbtype = libraryelement_fbtype;
    }
    public List<libraryElement_ServiceSequence> getLibraryelement_servicesequences() {
        return libraryelement_servicesequences;
    }

    public void addLibraryelement_servicesequence(Libraryelement_servicesequence libraryelement_servicesequence) {
        this.libraryelement_servicesequences.add(libraryelement_servicesequence);
    }
    public libraryElement_ServiceInterface getLibraryelement_serviceinterface() {
        return libraryelement_serviceinterface;
    }

    public void setLibraryelement_serviceinterface(libraryElement_ServiceInterface libraryelement_serviceinterface) {
        this.libraryelement_serviceinterface = libraryelement_serviceinterface;
    }
    public libraryElement_ServiceInterface getLibraryelement_serviceinterface() {
        return libraryelement_serviceinterface;
    }

    public void setLibraryelement_serviceinterface(libraryElement_ServiceInterface libraryelement_serviceinterface) {
        this.libraryelement_serviceinterface = libraryelement_serviceinterface;
    }

}