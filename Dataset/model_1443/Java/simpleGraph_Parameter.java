





import java.util.List;
import java.util.ArrayList;

public class simpleGraph_Parameter  {

    private String key;
    private String value;





    private simpleGraph_GraphElement simplegraph_graphelement;


    public simpleGraph_Parameter(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public simpleGraph_GraphElement getSimplegraph_graphelement() {
        return simplegraph_graphelement;
    }

    public void setSimplegraph_graphelement(simpleGraph_GraphElement simplegraph_graphelement) {
        this.simplegraph_graphelement = simplegraph_graphelement;
    }

}