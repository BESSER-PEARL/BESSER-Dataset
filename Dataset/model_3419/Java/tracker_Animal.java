




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class tracker_Animal  {

    private String breed;
    private String speciesCode;
    private LocalDate birthDate;
    private String weightGainPerDay;
    private String weight;
    private String age;
    private String species;
    private LocalDate lastEventDateTime;
    private String id;
    private String sex;
    private String sexCode;
    private String comments;





    private tracker_Animal tracker_animal;




    private tracker_Animal tracker_animal;


    public tracker_Animal(
        String breed,        String speciesCode,        LocalDate birthDate,        String weightGainPerDay,        String weight,        String age,        String species,        LocalDate lastEventDateTime,        String id,        String sex,        String sexCode,        String comments    ) {
        this.breed = breed;
        this.speciesCode = speciesCode;
        this.birthDate = birthDate;
        this.weightGainPerDay = weightGainPerDay;
        this.weight = weight;
        this.age = age;
        this.species = species;
        this.lastEventDateTime = lastEventDateTime;
        this.id = id;
        this.sex = sex;
        this.sexCode = sexCode;
        this.comments = comments;
    }


    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }
    public String getSpeciescode() {
        return speciesCode;
    }

    public void setSpeciescode(String speciesCode) {
        this.speciesCode = speciesCode;
    }
    public LocalDate getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(LocalDate birthDate) {
        this.birthDate = birthDate;
    }
    public String getWeightgainperday() {
        return weightGainPerDay;
    }

    public void setWeightgainperday(String weightGainPerDay) {
        this.weightGainPerDay = weightGainPerDay;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }
    public String getSpecies() {
        return species;
    }

    public void setSpecies(String species) {
        this.species = species;
    }
    public LocalDate getLasteventdatetime() {
        return lastEventDateTime;
    }

    public void setLasteventdatetime(LocalDate lastEventDateTime) {
        this.lastEventDateTime = lastEventDateTime;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }

    public tracker_Animal getTracker_animal() {
        return tracker_animal;
    }

    public void setTracker_animal(tracker_Animal tracker_animal) {
        this.tracker_animal = tracker_animal;
    }
    public tracker_Animal getTracker_animal() {
        return tracker_animal;
    }

    public void setTracker_animal(tracker_Animal tracker_animal) {
        this.tracker_animal = tracker_animal;
    }

}