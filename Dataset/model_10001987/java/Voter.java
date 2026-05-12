





import java.util.List;
import java.util.ArrayList;

public class Voter  {

    private String Name;
    private String Address;
    private boolean Eligibilty;
    private int student_faculty_ID;
    private int Age;



    public Voter(
        String Name,        String Address,        boolean Eligibilty,        int student_faculty_ID,        int Age    ) {
        this.Name = Name;
        this.Address = Address;
        this.Eligibilty = Eligibilty;
        this.student_faculty_ID = student_faculty_ID;
        this.Age = Age;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public boolean getEligibilty() {
        return Eligibilty;
    }

    public void setEligibilty(boolean Eligibilty) {
        this.Eligibilty = Eligibilty;
    }
    public int getStudent_faculty_id() {
        return student_faculty_ID;
    }

    public void setStudent_faculty_id(int student_faculty_ID) {
        this.student_faculty_ID = student_faculty_ID;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }


}