





import java.util.List;
import java.util.ArrayList;

public class libraryElement_Segment extends PositionableElement, TypedConfigureableObject, ColorizableElement {

    private String width;





    private List<libraryElement_Link> libraryelement_links;




    private libraryElement_Link libraryelement_link;




    private List<libraryElement_VarDeclaration> libraryelement_vardeclarations;


    public libraryElement_Segment(
        String width    ) {
        super(
        );
        this.width = width;
        this.libraryelement_links = new ArrayList<>();
        this.libraryelement_vardeclarations = new ArrayList<>();
    }

    public libraryElement_Segment(
        String width        ArrayList<libraryElement_Link> libraryelement_links,        ArrayList<libraryElement_VarDeclaration> libraryelement_vardeclarations    ) {
        this.width = width;
        this.libraryelement_links = libraryelement_links;
        this.libraryelement_vardeclarations = libraryelement_vardeclarations;
    }

    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }

    public List<libraryElement_Link> getLibraryelement_links() {
        return libraryelement_links;
    }

    public void addLibraryelement_link(Libraryelement_link libraryelement_link) {
        this.libraryelement_links.add(libraryelement_link);
    }
    public libraryElement_Link getLibraryelement_link() {
        return libraryelement_link;
    }

    public void setLibraryelement_link(libraryElement_Link libraryelement_link) {
        this.libraryelement_link = libraryelement_link;
    }
    public List<libraryElement_VarDeclaration> getLibraryelement_vardeclarations() {
        return libraryelement_vardeclarations;
    }

    public void addLibraryelement_vardeclaration(Libraryelement_vardeclaration libraryelement_vardeclaration) {
        this.libraryelement_vardeclarations.add(libraryelement_vardeclaration);
    }

}