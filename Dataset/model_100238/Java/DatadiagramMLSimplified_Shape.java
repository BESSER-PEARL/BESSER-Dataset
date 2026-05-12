





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLSimplified_Shape  {

    private String textStyle;
    private String lineStyle;
    private String fillStyle;



    public DatadiagramMLSimplified_Shape(
        String textStyle,        String lineStyle,        String fillStyle    ) {
        this.textStyle = textStyle;
        this.lineStyle = lineStyle;
        this.fillStyle = fillStyle;
    }


    public String getTextstyle() {
        return textStyle;
    }

    public void setTextstyle(String textStyle) {
        this.textStyle = textStyle;
    }
    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }
    public String getFillstyle() {
        return fillStyle;
    }

    public void setFillstyle(String fillStyle) {
        this.fillStyle = fillStyle;
    }


}