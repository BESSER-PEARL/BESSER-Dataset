





import java.util.List;
import java.util.ArrayList;

public class library_ReferenceNetwork extends Base {

    private String name;
    private String description;





    private List<library_NodeType> library_nodetypes;




    private library_ReferenceNetwork library_referencenetwork;


    public library_ReferenceNetwork(
        String name,        String description    ) {
        super(
        );
        this.name = name;
        this.description = description;
        this.library_nodetypes = new ArrayList<>();
    }

    public library_ReferenceNetwork(
        String name,        String description        ArrayList<library_NodeType> library_nodetypes    ) {
        this.name = name;
        this.description = description;
        this.library_nodetypes = library_nodetypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<library_NodeType> getLibrary_nodetypes() {
        return library_nodetypes;
    }

    public void addLibrary_nodetype(Library_nodetype library_nodetype) {
        this.library_nodetypes.add(library_nodetype);
    }
    public library_ReferenceNetwork getLibrary_referencenetwork() {
        return library_referencenetwork;
    }

    public void setLibrary_referencenetwork(library_ReferenceNetwork library_referencenetwork) {
        this.library_referencenetwork = library_referencenetwork;
    }

}