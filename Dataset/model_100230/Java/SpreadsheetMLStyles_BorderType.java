





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_BorderType  {

    private String lineStyle;
    private String color;
    private String position;
    private String weight;





    private BordersType borderstype;


    public SpreadsheetMLStyles_BorderType(
        String lineStyle,        String color,        String position,        String weight    ) {
        this.lineStyle = lineStyle;
        this.color = color;
        this.position = position;
        this.weight = weight;
    }


    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }

    public BordersType getBorderstype() {
        return borderstype;
    }

    public void setBorderstype(BordersType borderstype) {
        this.borderstype = borderstype;
    }

}