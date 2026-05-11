





import java.util.List;
import java.util.ArrayList;

public class crom_l1_composed_Relationship extends Relation, NamedElement {

    private String direction;



    public crom_l1_composed_Relationship(
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