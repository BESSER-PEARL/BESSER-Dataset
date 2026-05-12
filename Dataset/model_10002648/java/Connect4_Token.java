





import java.util.List;
import java.util.ArrayList;

public class Connect4_Token  {

    private boolean isEmpty;
    private String color;
    private int xValue;
    private int yValue;



    public Connect4_Token(
        boolean isEmpty,        String color,        int xValue,        int yValue    ) {
        this.isEmpty = isEmpty;
        this.color = color;
        this.xValue = xValue;
        this.yValue = yValue;
    }


    public boolean getIsempty() {
        return isEmpty;
    }

    public void setIsempty(boolean isEmpty) {
        this.isEmpty = isEmpty;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public int getXvalue() {
        return xValue;
    }

    public void setXvalue(int xValue) {
        this.xValue = xValue;
    }
    public int getYvalue() {
        return yValue;
    }

    public void setYvalue(int yValue) {
        this.yValue = yValue;
    }


}