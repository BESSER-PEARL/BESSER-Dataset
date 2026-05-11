





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BPMNRelationship extends BaseElement {

    private String type;
    private String direction;



    public BPMNProfile_BPMNRelationship(
        String type,        String direction    ) {
        super(
        );
        this.type = type;
        this.direction = direction;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }


}