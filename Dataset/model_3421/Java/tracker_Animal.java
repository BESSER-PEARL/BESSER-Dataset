





import java.util.List;
import java.util.ArrayList;

public class tracker_Animal  {

    private String idNumber;
    private String breed;
    private String birthDate;
    private String age;
    private String sex;
    private String species;
    private String sexCode;
    private String speciesCode;



    public tracker_Animal(
        String idNumber,        String breed,        String birthDate,        String age,        String sex,        String species,        String sexCode,        String speciesCode    ) {
        this.idNumber = idNumber;
        this.breed = breed;
        this.birthDate = birthDate;
        this.age = age;
        this.sex = sex;
        this.species = species;
        this.sexCode = sexCode;
        this.speciesCode = speciesCode;
    }


    public String getIdnumber() {
        return idNumber;
    }

    public void setIdnumber(String idNumber) {
        this.idNumber = idNumber;
    }
    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }
    public String getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(String birthDate) {
        this.birthDate = birthDate;
    }
    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }
    public String getSpecies() {
        return species;
    }

    public void setSpecies(String species) {
        this.species = species;
    }
    public String getSexcode() {
        return sexCode;
    }

    public void setSexcode(String sexCode) {
        this.sexCode = sexCode;
    }
    public String getSpeciescode() {
        return speciesCode;
    }

    public void setSpeciescode(String speciesCode) {
        this.speciesCode = speciesCode;
    }


}