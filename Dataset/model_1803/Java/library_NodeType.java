





import java.util.List;
import java.util.ArrayList;

public class library_NodeType extends Base {

    private String leafNode;
    private String name;





    private library_ProductInfo library_productinfo;


    public library_NodeType(
        String leafNode,        String name    ) {
        super(
        );
        this.leafNode = leafNode;
        this.name = name;
    }


    public String getLeafnode() {
        return leafNode;
    }

    public void setLeafnode(String leafNode) {
        this.leafNode = leafNode;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public library_ProductInfo getLibrary_productinfo() {
        return library_productinfo;
    }

    public void setLibrary_productinfo(library_ProductInfo library_productinfo) {
        this.library_productinfo = library_productinfo;
    }

}