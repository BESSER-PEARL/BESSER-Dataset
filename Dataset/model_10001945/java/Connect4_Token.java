





import java.util.List;
import java.util.ArrayList;

public class Connect4_Token  {

    private int yValue;
    private boolean isEmpty;
    private String color;
    private int xValue;



    public Connect4_Token(
        int yValue,        boolean isEmpty,        String color,        int xValue    ) {
        this.yValue = yValue;
        this.isEmpty = isEmpty;
        this.color = color;
        this.xValue = xValue;
    }


    public int getYvalue() {
        return yValue;
    }

    public void setYvalue(int yValue) {
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


}