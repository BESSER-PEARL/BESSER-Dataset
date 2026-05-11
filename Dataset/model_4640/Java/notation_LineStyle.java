





import java.util.List;
import java.util.ArrayList;

public class notation_LineStyle extends Style {

    private int lineWidth;
    private int lineColor;



    public notation_LineStyle(
        int lineWidth,        int lineColor    ) {
        super(
        );
        this.lineWidth = lineWidth;
        this.lineColor = lineColor;
    }


    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }
    public int getLinecolor() {
        return lineColor;
    }

    public void setLinecolor(int lineColor) {
        this.lineColor = lineColor;
    }


}