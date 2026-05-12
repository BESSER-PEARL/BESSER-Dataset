





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String Birthdate;
    private int Age;
    private String Name;
    private String Gender;
    private String DateOfEntry;
    private int PatientId;
    private String Sickness;



    public Patient(
        String Birthdate,        int Age,        String Name,        String Gender,        String DateOfEntry,        int PatientId,        String Sickness    ) {
        this.Birthdate = Birthdate;
        this.Age = Age;
        this.Name = Name;
        this.Gender = Gender;
        this.DateOfEntry = DateOfEntry;
        this.PatientId = PatientId;
        this.Sickness = Sickness;
    }


    public String getBirthdate() {
        return Birthdate;
    }

    public void setBirthdate(String Birthdate) {
        this.Birthdate = Birthdate;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
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
    public String getDateofentry() {
        return DateOfEntry;
    }

    public void setDateofentry(String DateOfEntry) {
        this.DateOfEntry = DateOfEntry;
    }
    public int getPatientid() {
        return PatientId;
    }

    public void setPatientid(int PatientId) {
        this.PatientId = PatientId;
    }
    public String getSickness() {
        return Sickness;
    }

    public void setSickness(String Sickness) {
        this.Sickness = Sickness;
    }


}