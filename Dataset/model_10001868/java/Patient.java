





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String name;
    private int age;
    private String accepted;
    private String prescriptions;
    private String sickness;
    private String allergies;
    private String id;
    private String specialReqs;
    private String gender;
    private String birthDate;



    public Patient(
        String name,        int age,        String accepted,        String prescriptions,        String sickness,        String allergies,        String id,        String specialReqs,        String gender,        String birthDate    ) {
        this.name = name;
        this.age = age;
        this.accepted = accepted;
        this.prescriptions = prescriptions;
        this.sickness = sickness;
        this.allergies = allergies;
        this.id = id;
        this.specialReqs = specialReqs;
        this.gender = gender;
        this.birthDate = birthDate;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public String getAccepted() {
        return accepted;
    }

    public void setAccepted(String accepted) {
        this.accepted = accepted;
    }
    public String getPrescriptions() {
        return prescriptions;
    }

    public void setPrescriptions(String prescriptions) {
        this.prescriptions = prescriptions;
    }
    public String getSickness() {
        return sickness;
    }

    public void setSickness(String sickness) {
        this.sickness = sickness;
    }
    public String getAllergies() {
        return allergies;
    }

    public void setAllergies(String allergies) {
        this.allergies = allergies;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSpecialreqs() {
        return specialReqs;
    }

    public void setSpecialreqs(String specialReqs) {
        this.specialReqs = specialReqs;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(String birthDate) {
        this.birthDate = birthDate;
    }


}