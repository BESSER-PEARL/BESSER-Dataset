





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_Parameter extends Kernel_MultiplicityElement, Kernel_TypedElement {

    private String direction;



    public fuml_Kernel_Parameter(
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