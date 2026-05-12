





import java.util.List;
import java.util.ArrayList;

public class Docter  {

    private String Salary;
    private int ID;
    private String Rank;
    private String Name;
    private String Specialization;
    private String attribute2;



    public Docter(
        String Salary,        int ID,        String Rank,        String Name,        String Specialization,        String attribute2    ) {
        this.Salary = Salary;
        this.ID = ID;
        this.Rank = Rank;
        this.Name = Name;
        this.Specialization = Specialization;
        this.attribute2 = attribute2;
    }


    public String getSalary() {
        return Salary;
    }

    public void setSalary(String Salary) {
        this.Salary = Salary;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getRank() {
        return Rank;
    }

    public void setRank(String Rank) {
        this.Rank = Rank;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getSpecialization() {
        return Specialization;
    }

    public void setSpecialization(String Specialization) {
        this.Specialization = Specialization;
    }
    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }


}