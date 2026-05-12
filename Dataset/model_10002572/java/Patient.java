





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String birthDate;
    private String gender;
    private String name;
    private String id;
    private String prescriptions;
    private String allergies;
    private int age;
    private String sickness;
    private String specialReqs;
    private String accepted;



    public Patient(
        String birthDate,        String gender,        String name,        String id,        String prescriptions,        String allergies,        int age,        String sickness,        String specialReqs,        String accepted    ) {
        this.birthDate = birthDate;
        this.gender = gender;
        this.name = name;
        this.id = id;
        this.prescriptions = prescriptions;
        this.allergies = allergies;
        this.age = age;
        this.sickness = sickness;
        this.specialReqs = specialReqs;
        this.accepted = accepted;
    }


    public String getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(String birthDate) {
        this.birthDate = birthDate;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPrescriptions() {
        return prescriptions;
    }

    public void setPrescriptions(String prescriptions) {
        this.prescriptions = prescriptions;
    }
    public String getAllergies() {
        return allergies;
    }

    public void setAllergies(String allergies) {
        this.allergies = allergies;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public String getSickness() {
        return sickness;
    }

    public void setSickness(String sickness) {
        this.sickness = sickness;
    }
    public String getSpecialreqs() {
        return specialReqs;
    }

    public void setSpecialreqs(String specialReqs) {
        this.specialReqs = specialReqs;
    }
    public String getAccepted() {
        return accepted;
    }

    public void setAccepted(String accepted) {
        this.accepted = accepted;
    }


}