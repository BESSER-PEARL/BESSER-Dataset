





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLTextFormat_Shape  {

    private String textStyle;
    private String fillStyle;
    private String lineStyle;



    public DatadiagramMLTextFormat_Shape(
        String textStyle,        String fillStyle,        String lineStyle    ) {
        this.textStyle = textStyle;
        this.fillStyle = fillStyle;
        this.lineStyle = lineStyle;
    }


    public String getTextstyle() {
        return textStyle;
    }

    public void setTextstyle(String textStyle) {
        this.textStyle = textStyle;
    }
    public String getFillstyle() {
        return fillStyle;
    }

    public void setFillstyle(String fillStyle) {
        this.fillStyle = fillStyle;
    }
    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }


}