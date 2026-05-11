





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Relationship extends BaseElement {

    private String direction;
    private String type;



    public bpmn2_Relationship(
        String direction,        String type    ) {
        super(
        );
        this.direction = direction;
        this.type = type;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}