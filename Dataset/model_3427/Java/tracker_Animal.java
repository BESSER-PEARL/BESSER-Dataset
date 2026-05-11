




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class tracker_Animal  {

    private String weightGainPerDay;
    private LocalDate lastEventDateTime;
    private LocalDate birthDate;
    private String sex;
    private String sexCode;
    private String visualID;
    private String speciesCode;
    private String comments;
    private String type;
    private String breed;
    private int ageInDays;
    private String alternativeID;
    private String species;
    private String weight;
    private String id;





    private tracker_Animal tracker_animal;




    private tracker_Animal tracker_animal;




    private tracker_Premises tracker_premises;




    private List<tracker_Tag> tracker_tags;


    public tracker_Animal(
        String weightGainPerDay,        LocalDate lastEventDateTime,        LocalDate birthDate,        String sex,        String sexCode,        String visualID,        String speciesCode,        String comments,        String type,        String breed,        int ageInDays,        String alternativeID,        String species,        String weight,        String id    ) {
        this.weightGainPerDay = weightGainPerDay;
        this.lastEventDateTime = lastEventDateTime;
        this.birthDate = birthDate;
        this.sex = sex;
        this.sexCode = sexCode;
        this.visualID = visualID;
        this.speciesCode = speciesCode;
        this.comments = comments;
        this.type = type;
        this.breed = breed;
        this.ageInDays = ageInDays;
        this.alternativeID = alternativeID;
        this.species = species;
        this.weight = weight;
        this.id = id;
        this.tracker_tags = new ArrayList<>();
    }

    public tracker_Animal(
        String weightGainPerDay,        LocalDate lastEventDateTime,        LocalDate birthDate,        String sex,        String sexCode,        String visualID,        String speciesCode,        String comments,        String type,        String breed,        int ageInDays,        String alternativeID,        String species,        String weight,        String id        ArrayList<tracker_Tag> tracker_tags    ) {
        this.weightGainPerDay = weightGainPerDay;
        this.lastEventDateTime = lastEventDateTime;
        this.birthDate = birthDate;
        this.sex = sex;
        this.sexCode = sexCode;
        this.visualID = visualID;
        this.speciesCode = speciesCode;
        this.comments = comments;
        this.type = type;
        this.breed = breed;
        this.ageInDays = ageInDays;
        this.alternativeID = alternativeID;
        this.species = species;
        this.weight = weight;
        this.id = id;
        this.tracker_tags = tracker_tags;
    }

    public String getWeightgainperday() {
        return weightGainPerDay;
    }

    public void setWeightgainperday(String weightGainPerDay) {
        this.weightGainPerDay = weightGainPerDay;
    }
    public LocalDate getLasteventdatetime() {
        return lastEventDateTime;
    }

    public void setLasteventdatetime(LocalDate lastEventDateTime) {
        this.lastEventDateTime = lastEventDateTime;
    }
    public LocalDate getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(LocalDate birthDate) {
        this.birthDate = birthDate;
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
    public String getVisualid() {
        return visualID;
    }

    public void setVisualid(String visualID) {
        this.visualID = visualID;
    }
    public String getSpeciescode() {
        return speciesCode;
    }

    public void setSpeciescode(String speciesCode) {
        this.speciesCode = speciesCode;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }
    public int getAgeindays() {
        return ageInDays;
    }

    public void setAgeindays(int ageInDays) {
        this.ageInDays = ageInDays;
    }
    public String getAlternativeid() {
        return alternativeID;
    }

    public void setAlternativeid(String alternativeID) {
        this.alternativeID = alternativeID;
    }
    public String getSpecies() {
        return species;
    }

    public void setSpecies(String species) {
        this.species = species;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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
    public tracker_Premises getTracker_premises() {
        return tracker_premises;
    }

    public void setTracker_premises(tracker_Premises tracker_premises) {
        this.tracker_premises = tracker_premises;
    }
    public List<tracker_Tag> getTracker_tags() {
        return tracker_tags;
    }

    public void addTracker_tag(Tracker_tag tracker_tag) {
        this.tracker_tags.add(tracker_tag);
    }

}