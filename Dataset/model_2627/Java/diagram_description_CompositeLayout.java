





import java.util.List;
import java.util.ArrayList;

public class diagram_description_CompositeLayout extends Layout {

    private int padding;
    private String direction;



    public diagram_description_CompositeLayout(
        int padding,        String direction    ) {
        super(
        );
        this.padding = padding;
        this.direction = direction;
    }


    public int getPadding() {
        return padding;
    }

    public void setPadding(int padding) {
        this.padding = padding;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }


}