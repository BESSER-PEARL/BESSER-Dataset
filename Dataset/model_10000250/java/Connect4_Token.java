





import java.util.List;
import java.util.ArrayList;

public class Connect4_Token  {

    private int yValue;
    private int xValue;
    private String color;
    private boolean isEmpty;



    public Connect4_Token(
        int yValue,        int xValue,        String color,        boolean isEmpty    ) {
        this.yValue = yValue;
        this.xValue = xValue;
        this.color = color;
        this.isEmpty = isEmpty;
    }


    public int getYvalue() {
        return yValue;
    }

    public void setYvalue(int yValue) {
        this.yValue = yValue;
    }
    public int getXvalue() {
        return xValue;
    }

    public void setXvalue(int xValue) {
        this.xValue = xValue;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public boolean getIsempty() {
        return isEmpty;
    }

    public void setIsempty(boolean isEmpty) {
        this.isEmpty = isEmpty;
    }


}