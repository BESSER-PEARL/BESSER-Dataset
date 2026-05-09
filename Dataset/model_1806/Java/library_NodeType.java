





import java.util.List;
import java.util.ArrayList;

public class library_NodeType extends Base {

    private String name;
    private String leafNode;



    public library_NodeType(
        String name,        String leafNode    ) {
        super(
        );
        this.name = name;
        this.leafNode = leafNode;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLeafnode() {
        return leafNode;
    }

    public void setLeafnode(String leafNode) {
        this.leafNode = leafNode;
    }


}