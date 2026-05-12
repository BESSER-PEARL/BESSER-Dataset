





import java.util.List;
import java.util.ArrayList;

public class Course3  {

    private int Id;
    private String Name;
    private String StartDate;



    public Course3(
        int Id,        String Name,        String StartDate    ) {
        this.Id = Id;
        this.Name = Name;
        this.StartDate = StartDate;
    }


    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getStartdate() {
        return StartDate;
    }

    public void setStartdate(String StartDate) {
        this.StartDate = StartDate;
    }


}