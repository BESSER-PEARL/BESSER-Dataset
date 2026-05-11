





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Relationship extends BaseElement {

    private String type;
    private String direction;



    public BPMN2Model_Relationship(
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