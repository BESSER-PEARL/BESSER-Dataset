





import java.util.List;
import java.util.ArrayList;

public class library_ReferenceRelationship extends Base {

    private String name;





    private library_NodeType library_nodetype;




    private library_NodeType library_nodetype;




    private library_ReferenceNetwork library_referencenetwork;


    public library_ReferenceRelationship(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public library_NodeType getLibrary_nodetype() {
        return library_nodetype;
    }

    public void setLibrary_nodetype(library_NodeType library_nodetype) {
        this.library_nodetype = library_nodetype;
    }
    public library_NodeType getLibrary_nodetype() {
        return library_nodetype;
    }

    public void setLibrary_nodetype(library_NodeType library_nodetype) {
        this.library_nodetype = library_nodetype;
    }
    public library_ReferenceNetwork getLibrary_referencenetwork() {
        return library_referencenetwork;
    }

    public void setLibrary_referencenetwork(library_ReferenceNetwork library_referencenetwork) {
        this.library_referencenetwork = library_referencenetwork;
    }

}