





import java.util.List;
import java.util.ArrayList;

public class model_LineStyle extends Feature {

    private boolean manhattan;
    private String style;



    public model_LineStyle(
        boolean manhattan,        String style    ) {
        super(
        );
        this.manhattan = manhattan;
        this.style = style;
    }


    public boolean getManhattan() {
        return manhattan;
    }

    public void setManhattan(boolean manhattan) {
        this.manhattan = manhattan;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }


}