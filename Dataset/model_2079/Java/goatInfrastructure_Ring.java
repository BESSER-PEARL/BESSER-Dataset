





import java.util.List;
import java.util.ArrayList;

public class goatInfrastructure_Ring extends Infrastructure {

    private String mid_assigner;
    private String nodes;
    private String registration;



    public goatInfrastructure_Ring(
        String mid_assigner,        String nodes,        String registration    ) {
        super(
        );
        this.mid_assigner = mid_assigner;
        this.nodes = nodes;
        this.registration = registration;
    }


    public String getMid_assigner() {
        return mid_assigner;
    }

    public void setMid_assigner(String mid_assigner) {
        this.mid_assigner = mid_assigner;
    }
    public String getNodes() {
        return nodes;
    }

    public void setNodes(String nodes) {
        this.nodes = nodes;
    }
    public String getRegistration() {
        return registration;
    }

    public void setRegistration(String registration) {
        this.registration = registration;
    }


}