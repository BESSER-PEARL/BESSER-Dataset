





import java.util.List;
import java.util.ArrayList;

public class model_Line extends FeatureContainer {

    private boolean horizontal;
    private boolean vertical;



    public model_Line(
        boolean horizontal,        boolean vertical    ) {
        super(
        );
        this.horizontal = horizontal;
        this.vertical = vertical;
    }


    public boolean getHorizontal() {
        return horizontal;
    }

    public void setHorizontal(boolean horizontal) {
        this.horizontal = horizontal;
    }
    public boolean getVertical() {
        return vertical;
    }

    public void setVertical(boolean vertical) {
        this.vertical = vertical;
    }


}