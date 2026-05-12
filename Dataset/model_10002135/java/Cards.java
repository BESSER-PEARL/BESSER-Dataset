





import java.util.List;
import java.util.ArrayList;

public class Cards  {

    private String number;
    private String color;



    public Cards(
        String number,        String color    ) {
        this.number = number;
        this.color = color;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }


}