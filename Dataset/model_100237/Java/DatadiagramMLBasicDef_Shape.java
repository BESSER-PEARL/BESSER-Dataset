





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLBasicDef_Shape  {

    private String lineStyle;
    private String textStyle;
    private String fillStyle;



    public DatadiagramMLBasicDef_Shape(
        String lineStyle,        String textStyle,        String fillStyle    ) {
        this.lineStyle = lineStyle;
        this.textStyle = textStyle;
        this.fillStyle = fillStyle;
    }


    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
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


}