





import java.util.List;
import java.util.ArrayList;

public class goatInfrastructure_Cluster extends Infrastructure {

    private String message_queue;
    private String mid_assigner;
    private String registration;
    private String nodes;



    public goatInfrastructure_Cluster(
        String message_queue,        String mid_assigner,        String registration,        String nodes    ) {
        super(
        );
        this.message_queue = message_queue;
        this.mid_assigner = mid_assigner;
        this.registration = registration;
        this.nodes = nodes;
    }


    public String getMessage_queue() {
        return message_queue;
    }

    public void setMessage_queue(String message_queue) {
        this.message_queue = message_queue;
    }
    public String getMid_assigner() {
        return mid_assigner;
    }

    public void setMid_assigner(String mid_assigner) {
        this.mid_assigner = mid_assigner;
    }
    public String getRegistration() {
        return registration;
    }

    public void setRegistration(String registration) {
        this.registration = registration;
    }
    public String getNodes() {
        return nodes;
    }

    public void setNodes(String nodes) {
        this.nodes = nodes;
    }


}