





import java.util.List;
import java.util.ArrayList;

public class Course2  {

    private int Id;
    private String StartDate;
    private String Name;



    public Course2(
        int Id,        String StartDate,        String Name    ) {
        this.Id = Id;
        this.StartDate = StartDate;
        this.Name = Name;
    }


    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public String getStartdate() {
        return StartDate;
    }

    public void setStartdate(String StartDate) {
        this.StartDate = StartDate;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}