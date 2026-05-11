





import java.util.List;
import java.util.ArrayList;

public class trnet_AttributePattern  {

    private String name;





    private trnet_NodePattern trnet_nodepattern;


    public trnet_AttributePattern(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public trnet_NodePattern getTrnet_nodepattern() {
        return trnet_nodepattern;
    }

    public void setTrnet_nodepattern(trnet_NodePattern trnet_nodepattern) {
        this.trnet_nodepattern = trnet_nodepattern;
    }

}