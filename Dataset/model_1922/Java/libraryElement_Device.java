





import java.util.List;
import java.util.ArrayList;

public class libraryElement_Device extends PositionableElement, TypedConfigureableObject, IVarElement, ColorizableElement {

    private String profile;





    private libraryElement_Link libraryelement_link;




    private List<libraryElement_Link> libraryelement_links;


    public libraryElement_Device(
        String profile    ) {
        super(
        );
        this.profile = profile;
        this.libraryelement_links = new ArrayList<>();
    }

    public libraryElement_Device(
        String profile        ArrayList<libraryElement_Link> libraryelement_links    ) {
        this.profile = profile;
        this.libraryelement_links = libraryelement_links;
    }

    public String getProfile() {
        return profile;
    }

    public void setProfile(String profile) {
        this.profile = profile;
    }

    public libraryElement_Link getLibraryelement_link() {
        return libraryelement_link;
    }

    public void setLibraryelement_link(libraryElement_Link libraryelement_link) {
        this.libraryelement_link = libraryelement_link;
    }
    public List<libraryElement_Link> getLibraryelement_links() {
        return libraryelement_links;
    }

    public void addLibraryelement_link(Libraryelement_link libraryelement_link) {
        this.libraryelement_links.add(libraryelement_link);
    }

}