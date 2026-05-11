





import java.util.List;
import java.util.ArrayList;

public class eSport_Tournament  {

    private int size;
    private int year;
    private String type;
    private String name;



    public eSport_Tournament(
        int size,        int year,        String type,        String name    ) {
        this.size = size;
        this.year = year;
        this.type = type;
        this.name = name;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}