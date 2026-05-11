





import java.util.List;
import java.util.ArrayList;

public class model_LineObject  {

    private int lineWidth;
    private String lineColor;



    public model_LineObject(
        int lineWidth,        String lineColor    ) {
        this.lineWidth = lineWidth;
        this.lineColor = lineColor;
    }


    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }
    public String getLinecolor() {
        return lineColor;
    }

    public void setLinecolor(String lineColor) {
        this.lineColor = lineColor;
    }


}