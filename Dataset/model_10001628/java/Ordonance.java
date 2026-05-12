





import java.util.List;
import java.util.ArrayList;

public class Ordonance  {

    private String date;
    private int id;



    public Ordonance(
        String date,        int id    ) {
        this.date = date;
        this.id = id;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}