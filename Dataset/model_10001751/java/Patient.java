





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String Name;
    private String Gender;
    private int Age;
    private String Sickness;
    private int PatientId;
    private String DateOfEntry;
    private String Birthdate;



    public Patient(
        String Name,        String Gender,        int Age,        String Sickness,        int PatientId,        String DateOfEntry,        String Birthdate    ) {
        this.Name = Name;
        this.Gender = Gender;
        this.Age = Age;
        this.Sickness = Sickness;
        this.PatientId = PatientId;
        this.DateOfEntry = DateOfEntry;
        this.Birthdate = Birthdate;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }
    public String getSickness() {
        return Sickness;
    }

    public void setSickness(String Sickness) {
        this.Sickness = Sickness;
    }
    public int getPatientid() {
        return PatientId;
    }

    public void setPatientid(int PatientId) {
        this.PatientId = PatientId;
    }
    public String getDateofentry() {
        return DateOfEntry;
    }

    public void setDateofentry(String DateOfEntry) {
        this.DateOfEntry = DateOfEntry;
    }
    public String getBirthdate() {
        return Birthdate;
    }

    public void setBirthdate(String Birthdate) {
        this.Birthdate = Birthdate;
    }


}