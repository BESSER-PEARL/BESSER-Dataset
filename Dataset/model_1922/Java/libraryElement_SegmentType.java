





import java.util.List;
import java.util.ArrayList;

public class libraryElement_SegmentType extends CompilableType {






    private List<libraryElement_VarDeclaration> libraryelement_vardeclarations;


    public libraryElement_SegmentType(
    ) {
        super(
        );
        this.libraryelement_vardeclarations = new ArrayList<>();
    }

    public libraryElement_SegmentType(
        ArrayList<libraryElement_VarDeclaration> libraryelement_vardeclarations    ) {
        this.libraryelement_vardeclarations = libraryelement_vardeclarations;
    }


    public List<libraryElement_VarDeclaration> getLibraryelement_vardeclarations() {
        return libraryelement_vardeclarations;
    }

    public void addLibraryelement_vardeclaration(Libraryelement_vardeclaration libraryelement_vardeclaration) {
        this.libraryelement_vardeclarations.add(libraryelement_vardeclaration);
    }

}