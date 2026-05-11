





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_CompositeLayout extends Layout {

    private String direction;
    private int padding;



    public viewpoint_description_CompositeLayout(
        String direction,        int padding    ) {
        super(
        );
        this.direction = direction;
        this.padding = padding;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public int getPadding() {
        return padding;
    }

    public void setPadding(int padding) {
        this.padding = padding;
    }


}