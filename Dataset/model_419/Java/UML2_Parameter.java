





import java.util.List;
import java.util.ArrayList;

public class UML2_Parameter extends TypedElement, MultiplicityElement, ConnectableElement {

    private String direction;



    public UML2_Parameter(
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