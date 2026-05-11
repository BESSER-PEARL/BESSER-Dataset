





import java.util.List;
import java.util.ArrayList;

public class grapho_Edge extends GraphElement {

    private boolean constraintRank;
    private String style;
    private String color;



    public grapho_Edge(
        boolean constraintRank,        String style,        String color    ) {
        super(
        );
        this.constraintRank = constraintRank;
        this.style = style;
        this.color = color;
    }


    public boolean getConstraintrank() {
        return constraintRank;
    }

    public void setConstraintrank(boolean constraintRank) {
        this.constraintRank = constraintRank;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }


}