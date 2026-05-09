





import java.util.List;
import java.util.ArrayList;

public class libraryElement_ResourceType extends CompilableType {






    private libraryElement_FBNetwork libraryelement_fbnetwork;




    private libraryElement_FBType libraryelement_fbtype;




    private List<libraryElement_VarDeclaration> libraryelement_vardeclarations;


    public libraryElement_ResourceType(
    ) {
        super(
        );
        this.libraryelement_vardeclarations = new ArrayList<>();
    }

    public libraryElement_ResourceType(
        ArrayList<libraryElement_VarDeclaration> libraryelement_vardeclarations    ) {
        this.libraryelement_vardeclarations = libraryelement_vardeclarations;
    }


    public libraryElement_FBNetwork getLibraryelement_fbnetwork() {
        return libraryelement_fbnetwork;
    }

    public void setLibraryelement_fbnetwork(libraryElement_FBNetwork libraryelement_fbnetwork) {
        this.libraryelement_fbnetwork = libraryelement_fbnetwork;
    }
    public libraryElement_FBType getLibraryelement_fbtype() {
        return libraryelement_fbtype;
    }

    public void setLibraryelement_fbtype(libraryElement_FBType libraryelement_fbtype) {
        this.libraryelement_fbtype = libraryelement_fbtype;
    }
    public List<libraryElement_VarDeclaration> getLibraryelement_vardeclarations() {
        return libraryelement_vardeclarations;
    }

    public void addLibraryelement_vardeclaration(Libraryelement_vardeclaration libraryelement_vardeclaration) {
        this.libraryelement_vardeclarations.add(libraryelement_vardeclaration);
    }

}