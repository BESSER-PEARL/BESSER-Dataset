





import java.util.List;
import java.util.ArrayList;

public class statespace_Model  {

    private String resource;
    private int objectCount;
    private String eGraph;
    private String objectKeys;





    private statespace_State statespace_state;


    public statespace_Model(
        String resource,        int objectCount,        String eGraph,        String objectKeys    ) {
        this.resource = resource;
        this.objectCount = objectCount;
        this.eGraph = eGraph;
        this.objectKeys = objectKeys;
    }


    public String getResource() {
        return resource;
    }

    public void setResource(String resource) {
        this.resource = resource;
    }
    public int getObjectcount() {
        return objectCount;
    }

    public void setObjectcount(int objectCount) {
        this.objectCount = objectCount;
    }
    public String getEgraph() {
        return eGraph;
    }

    public void setEgraph(String eGraph) {
        this.eGraph = eGraph;
    }
    public String getObjectkeys() {
        return objectKeys;
    }

    public void setObjectkeys(String objectKeys) {
        this.objectKeys = objectKeys;
    }

    public statespace_State getStatespace_state() {
        return statespace_state;
    }

    public void setStatespace_state(statespace_State statespace_state) {
        this.statespace_state = statespace_state;
    }

}