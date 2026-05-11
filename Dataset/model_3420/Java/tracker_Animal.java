





import java.util.List;
import java.util.ArrayList;

public class tracker_Animal  {

    private String idNumber;
    private String sex;
    private String sexCode;
    private String birthDate;
    private String species;
    private String age;
    private String speciesCode;
    private String breed;



    public tracker_Animal(
        String idNumber,        String sex,        String sexCode,        String birthDate,        String species,        String age,        String speciesCode,        String breed    ) {
        this.idNumber = idNumber;
        this.sex = sex;
        this.sexCode = sexCode;
        this.birthDate = birthDate;
        this.species = species;
        this.age = age;
        this.speciesCode = speciesCode;
        this.breed = breed;
    }


    public String getIdnumber() {
        return idNumber;
    }

    public void setIdnumber(String idNumber) {
        this.idNumber = idNumber;
    }
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }
    public String getSexcode() {
        return sexCode;
    }

    public void setSexcode(String sexCode) {
        this.sexCode = sexCode;
    }
    public String getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(String birthDate) {
        this.birthDate = birthDate;
    }
    public String getSpecies() {
        return species;
    }

    public void setSpecies(String species) {
        this.species = species;
    }
    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }
    public String getSpeciescode() {
        return speciesCode;
    }

    public void setSpeciescode(String speciesCode) {
        this.speciesCode = speciesCode;
    }
    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }


}