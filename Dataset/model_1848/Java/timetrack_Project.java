





import java.util.List;
import java.util.ArrayList;

public class timetrack_Project  {

    private String number;
    private String name;





    private timetrack_Library timetrack_library;


    public timetrack_Project(
        String number,        String name    ) {
        this.number = number;
        this.name = name;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public timetrack_Library getTimetrack_library() {
        return timetrack_library;
    }

    public void setTimetrack_library(timetrack_Library timetrack_library) {
        this.timetrack_library = timetrack_library;
    }

}