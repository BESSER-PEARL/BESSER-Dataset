





import java.util.List;
import java.util.ArrayList;

public class model_Node  {

    private String nodeName;
    private String nodePrefix;



    public model_Node(
        String nodeName,        String nodePrefix    ) {
        this.nodeName = nodeName;
        this.nodePrefix = nodePrefix;
    }


    public String getNodename() {
        return nodeName;
    }

    public void setNodename(String nodeName) {
        this.nodeName = nodeName;
    }
    public String getNodeprefix() {
        return nodePrefix;
    }

    public void setNodeprefix(String nodePrefix) {
        this.nodePrefix = nodePrefix;
    }


}