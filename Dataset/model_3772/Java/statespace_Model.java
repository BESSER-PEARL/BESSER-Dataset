





import java.util.List;
import java.util.ArrayList;

public class statespace_Model  {

    private String eGraph;
    private int objectCount;
    private String objectKeys;
    private String resource;





    private statespace_State statespace_state;


    public statespace_Model(
        String eGraph,        int objectCount,        String objectKeys,        String resource    ) {
        this.eGraph = eGraph;
        this.objectCount = objectCount;
        this.objectKeys = objectKeys;
        this.resource = resource;
    }


    public String getEgraph() {
        return eGraph;
    }

    public void setEgraph(String eGraph) {
        this.eGraph = eGraph;
    }
    public int getObjectcount() {
        return objectCount;
    }

    public void setObjectcount(int objectCount) {
        this.objectCount = objectCount;
    }
    public String getObjectkeys() {
        return objectKeys;
    }

    public void setObjectkeys(String objectKeys) {
        this.objectKeys = objectKeys;
    }
    public String getResource() {
        return resource;
    }

    public void setResource(String resource) {
        this.resource = resource;
    }

    public statespace_State getStatespace_state() {
        return statespace_state;
    }

    public void setStatespace_state(statespace_State statespace_state) {
        this.statespace_state = statespace_state;
    }

}