





import java.util.List;
import java.util.ArrayList;

public class sparqlas_AnonymousIndividual extends Individual {

    private String nodeID;



    public sparqlas_AnonymousIndividual(
        String nodeID    ) {
        super(
        );
        this.nodeID = nodeID;
    }


    public String getNodeid() {
        return nodeID;
    }

    public void setNodeid(String nodeID) {
        this.nodeID = nodeID;
    }


}