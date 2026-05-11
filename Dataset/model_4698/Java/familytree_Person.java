




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class familytree_Person  {

    private String firstName;
    private LocalDate dayOfDeath;
    private boolean died;
    private LocalDate dayOfBirth;
    private String nameOfBirth;
    private String imagePaths;
    private String locationOfBirth;
    private String secondName;
    private String relationshipStatus;





    private List<familytree_Person> familytree_persons;




    private familytree_Person familytree_person;




    private familytree_Person familytree_person;




    private familytree_Person familytree_person;


    public familytree_Person(
        String firstName,        LocalDate dayOfDeath,        boolean died,        LocalDate dayOfBirth,        String nameOfBirth,        String imagePaths,        String locationOfBirth,        String secondName,        String relationshipStatus    ) {
        this.firstName = firstName;
        this.dayOfDeath = dayOfDeath;
        this.died = died;
        this.dayOfBirth = dayOfBirth;
        this.nameOfBirth = nameOfBirth;
        this.imagePaths = imagePaths;
        this.locationOfBirth = locationOfBirth;
        this.secondName = secondName;
        this.relationshipStatus = relationshipStatus;
        this.familytree_persons = new ArrayList<>();
    }

    public familytree_Person(
        String firstName,        LocalDate dayOfDeath,        boolean died,        LocalDate dayOfBirth,        String nameOfBirth,        String imagePaths,        String locationOfBirth,        String secondName,        String relationshipStatus        ArrayList<familytree_Person> familytree_persons    ) {
        this.firstName = firstName;
        this.dayOfDeath = dayOfDeath;
        this.died = died;
        this.dayOfBirth = dayOfBirth;
        this.nameOfBirth = nameOfBirth;
        this.imagePaths = imagePaths;
        this.locationOfBirth = locationOfBirth;
        this.secondName = secondName;
        this.relationshipStatus = relationshipStatus;
        this.familytree_persons = familytree_persons;
    }

    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public LocalDate getDayofdeath() {
        return dayOfDeath;
    }

    public void setDayofdeath(LocalDate dayOfDeath) {
        this.dayOfDeath = dayOfDeath;
    }
    public boolean getDied() {
        return died;
    }

    public void setDied(boolean died) {
        this.died = died;
    }
    public LocalDate getDayofbirth() {
        return dayOfBirth;
    }

    public void setDayofbirth(LocalDate dayOfBirth) {
        this.dayOfBirth = dayOfBirth;
    }
    public String getNameofbirth() {
        return nameOfBirth;
    }

    public void setNameofbirth(String nameOfBirth) {
        this.nameOfBirth = nameOfBirth;
    }
    public String getImagepaths() {
        return imagePaths;
    }

    public void setImagepaths(String imagePaths) {
        this.imagePaths = imagePaths;
    }
    public String getLocationofbirth() {
        return locationOfBirth;
    }

    public void setLocationofbirth(String locationOfBirth) {
        this.locationOfBirth = locationOfBirth;
    }
    public String getSecondname() {
        return secondName;
    }

    public void setSecondname(String secondName) {
        this.secondName = secondName;
    }
    public String getRelationshipstatus() {
        return relationshipStatus;
    }

    public void setRelationshipstatus(String relationshipStatus) {
        this.relationshipStatus = relationshipStatus;
    }

    public List<familytree_Person> getFamilytree_persons() {
        return familytree_persons;
    }

    public void addFamilytree_person(Familytree_person familytree_person) {
        this.familytree_persons.add(familytree_person);
    }
    public familytree_Person getFamilytree_person() {
        return familytree_person;
    }

    public void setFamilytree_person(familytree_Person familytree_person) {
        this.familytree_person = familytree_person;
    }
    public familytree_Person getFamilytree_person() {
        return familytree_person;
    }

    public void setFamilytree_person(familytree_Person familytree_person) {
        this.familytree_person = familytree_person;
    }
    public familytree_Person getFamilytree_person() {
        return familytree_person;
    }

    public void setFamilytree_person(familytree_Person familytree_person) {
        this.familytree_person = familytree_person;
    }

}