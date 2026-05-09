





import java.util.List;
import java.util.ArrayList;

public class sistedesMM_Edition  {

    private int year;
    private String location;



    public sistedesMM_Edition(
        int year,        String location    ) {
        this.year = year;
        this.location = location;
    }


    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}