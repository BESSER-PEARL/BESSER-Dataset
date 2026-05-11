





import java.util.List;
import java.util.ArrayList;

public class services_ServiceFlowRelationship extends Base {

    private String direction;



    public services_ServiceFlowRelationship(
        String direction    ) {
        super(
        );
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }


}