





import java.util.List;
import java.util.ArrayList;

public class notation_LineStyle extends Style {

    private int lineColor;
    private int lineWidth;



    public notation_LineStyle(
        int lineColor,        int lineWidth    ) {
        super(
        );
        this.lineColor = lineColor;
        this.lineWidth = lineWidth;
    }


    public int getLinecolor() {
        return lineColor;
    }

    public void setLinecolor(int lineColor) {
        this.lineColor = lineColor;
    }
    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }


}