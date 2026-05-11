





import java.util.List;
import java.util.ArrayList;

public class tracker_Animal  {

    private String id;
    private String species;
    private String breed;
    private String birthDate;
    private String sex;
    private String speciesCode;
    private String sexCode;
    private String age;
    private String idNumber;





    private List<tracker_Tag> tracker_tags;


    public tracker_Animal(
        String id,        String species,        String breed,        String birthDate,        String sex,        String speciesCode,        String sexCode,        String age,        String idNumber    ) {
        this.id = id;
        this.species = species;
        this.breed = breed;
        this.birthDate = birthDate;
        this.sex = sex;
        this.speciesCode = speciesCode;
        this.sexCode = sexCode;
        this.age = age;
        this.idNumber = idNumber;
        this.tracker_tags = new ArrayList<>();
    }

    public tracker_Animal(
        String id,        String species,        String breed,        String birthDate,        String sex,        String speciesCode,        String sexCode,        String age,        String idNumber        ArrayList<tracker_Tag> tracker_tags    ) {
        this.id = id;
        this.species = species;
        this.breed = breed;
        this.birthDate = birthDate;
        this.sex = sex;
        this.speciesCode = speciesCode;
        this.sexCode = sexCode;
        this.age = age;
        this.idNumber = idNumber;
        this.tracker_tags = tracker_tags;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSpecies() {
        return species;
    }

    public void setSpecies(String species) {
        this.species = species;
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
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }
    public String getSpeciescode() {
        return speciesCode;
    }

    public void setSpeciescode(String speciesCode) {
        this.speciesCode = speciesCode;
    }
    public String getSexcode() {
        return sexCode;
    }

    public void setSexcode(String sexCode) {
        this.sexCode = sexCode;
    }
    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }
    public String getIdnumber() {
        return idNumber;
    }

    public void setIdnumber(String idNumber) {
        this.idNumber = idNumber;
    }

    public List<tracker_Tag> getTracker_tags() {
        return tracker_tags;
    }

    public void addTracker_tag(Tracker_tag tracker_tag) {
        this.tracker_tags.add(tracker_tag);
    }

}