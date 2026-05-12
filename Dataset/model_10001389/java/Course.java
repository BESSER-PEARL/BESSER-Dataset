





import java.util.List;
import java.util.ArrayList;

public class Course  {

    private String Name;
    private int Id;
    private String StartDate;



    public Course(
        String Name,        int Id,        String StartDate    ) {
        this.Name = Name;
        this.Id = Id;
        this.StartDate = StartDate;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
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


}