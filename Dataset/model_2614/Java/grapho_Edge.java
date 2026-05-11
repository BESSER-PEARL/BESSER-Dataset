





import java.util.List;
import java.util.ArrayList;

public class grapho_Edge extends GraphElement {

    private String style;
    private boolean constraintRank;
    private String color;



    public grapho_Edge(
        String style,        boolean constraintRank,        String color    ) {
        super(
        );
        this.style = style;
        this.constraintRank = constraintRank;
        this.color = color;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public boolean getConstraintrank() {
        return constraintRank;
    }

    public void setConstraintrank(boolean constraintRank) {
        this.constraintRank = constraintRank;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }


}