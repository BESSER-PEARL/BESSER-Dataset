





import java.util.List;
import java.util.ArrayList;

public class libraryElement_DeviceType extends CompilableType {

    private String profile;





    private List<libraryElement_Resource> libraryelement_resources;




    private List<libraryElement_VarDeclaration> libraryelement_vardeclarations;




    private libraryElement_FBNetwork libraryelement_fbnetwork;


    public libraryElement_DeviceType(
        String profile    ) {
        super(
        );
        this.profile = profile;
        this.libraryelement_resources = new ArrayList<>();
        this.libraryelement_vardeclarations = new ArrayList<>();
    }

    public libraryElement_DeviceType(
        String profile        ArrayList<libraryElement_Resource> libraryelement_resources,        ArrayList<libraryElement_VarDeclaration> libraryelement_vardeclarations    ) {
        this.profile = profile;
        this.libraryelement_resources = libraryelement_resources;
        this.libraryelement_vardeclarations = libraryelement_vardeclarations;
    }

    public String getProfile() {
        return profile;
    }

    public void setProfile(String profile) {
        this.profile = profile;
    }

    public List<libraryElement_Resource> getLibraryelement_resources() {
        return libraryelement_resources;
    }

    public void addLibraryelement_resource(Libraryelement_resource libraryelement_resource) {
        this.libraryelement_resources.add(libraryelement_resource);
    }
    public List<libraryElement_VarDeclaration> getLibraryelement_vardeclarations() {
        return libraryelement_vardeclarations;
    }

    public void addLibraryelement_vardeclaration(Libraryelement_vardeclaration libraryelement_vardeclaration) {
        this.libraryelement_vardeclarations.add(libraryelement_vardeclaration);
    }
    public libraryElement_FBNetwork getLibraryelement_fbnetwork() {
        return libraryelement_fbnetwork;
    }

    public void setLibraryelement_fbnetwork(libraryElement_FBNetwork libraryelement_fbnetwork) {
        this.libraryelement_fbnetwork = libraryelement_fbnetwork;
    }

}