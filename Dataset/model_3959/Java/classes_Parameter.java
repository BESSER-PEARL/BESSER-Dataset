





import java.util.List;
import java.util.ArrayList;

public class classes_Parameter extends TypedElement, MultiplicityElement {

    private String direction;



    public classes_Parameter(
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