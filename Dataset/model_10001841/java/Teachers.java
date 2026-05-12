





import java.util.List;
import java.util.ArrayList;

public class Teachers  {

    private None Department;
    private None ID;
    private None Course;
    private None Info;
    private None Rank;
    private String Name;





    private Administrator administrator;


    public Teachers(
        None Department,        None ID,        None Course,        None Info,        None Rank,        String Name    ) {
        this.Department = Department;
        this.ID = ID;
        this.Course = Course;
        this.Info = Info;
        this.Rank = Rank;
        this.Name = Name;
    }


    public None getDepartment() {
        return Department;
    }

    public void setDepartment(None Department) {
        this.Department = Department;
    }
    public None getId() {
        return ID;
    }

    public void setId(None ID) {
        this.ID = ID;
    }
    public None getCourse() {
        return Course;
    }

    public void setCourse(None Course) {
        this.Course = Course;
    }
    public None getInfo() {
        return Info;
    }

    public void setInfo(None Info) {
        this.Info = Info;
    }
    public None getRank() {
        return Rank;
    }

    public void setRank(None Rank) {
        this.Rank = Rank;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Administrator getAdministrator() {
        return administrator;
    }

    public void setAdministrator(Administrator administrator) {
        this.administrator = administrator;
    }

}