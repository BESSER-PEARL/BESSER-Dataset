





import java.util.List;
import java.util.ArrayList;

public class form_Column  {

    private String width;
    private int number;



    public form_Column(
        String width,        int number    ) {
        this.width = width;
        this.number = number;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }


}