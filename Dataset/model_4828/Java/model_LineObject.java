





import java.util.List;
import java.util.ArrayList;

public class model_LineObject  {

    private String lineColor;
    private int lineWidth;



    public model_LineObject(
        String lineColor,        int lineWidth    ) {
        this.lineColor = lineColor;
        this.lineWidth = lineWidth;
    }


    public String getLinecolor() {
        return lineColor;
    }

    public void setLinecolor(String lineColor) {
        this.lineColor = lineColor;
    }
    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }


}