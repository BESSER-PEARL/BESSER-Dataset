





import java.util.List;
import java.util.ArrayList;

public class model_Layout extends Feature {

    private boolean horizontal;
    private int margin;
    private boolean vertical;



    public model_Layout(
        boolean horizontal,        int margin,        boolean vertical    ) {
        super(
        );
        this.horizontal = horizontal;
        this.margin = margin;
        this.vertical = vertical;
    }


    public boolean getHorizontal() {
        return horizontal;
    }

    public void setHorizontal(boolean horizontal) {
        this.horizontal = horizontal;
    }
    public int getMargin() {
        return margin;
    }

    public void setMargin(int margin) {
        this.margin = margin;
    }
    public boolean getVertical() {
        return vertical;
    }

    public void setVertical(boolean vertical) {
        this.vertical = vertical;
    }


}