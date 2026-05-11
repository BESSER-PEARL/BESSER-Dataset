





import java.util.List;
import java.util.ArrayList;

public class pdb1_Person  {

    private String lastName;
    private String birthday;
    private String firstName;
    private String incrementalID;
    private String placeOfBirth;
    private String id;





    private pdb1_Database pdb1_database;




    private pdb1_Database pdb1_database;


    public pdb1_Person(
        String lastName,        String birthday,        String firstName,        String incrementalID,        String placeOfBirth,        String id    ) {
        this.lastName = lastName;
        this.birthday = birthday;
        this.firstName = firstName;
        this.incrementalID = incrementalID;
        this.placeOfBirth = placeOfBirth;
        this.id = id;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getBirthday() {
        return birthday;
    }

    public void setBirthday(String birthday) {
        this.birthday = birthday;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getIncrementalid() {
        return incrementalID;
    }

    public void setIncrementalid(String incrementalID) {
        this.incrementalID = incrementalID;
    }
    public String getPlaceofbirth() {
        return placeOfBirth;
    }

    public void setPlaceofbirth(String placeOfBirth) {
        this.placeOfBirth = placeOfBirth;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public pdb1_Database getPdb1_database() {
        return pdb1_database;
    }

    public void setPdb1_database(pdb1_Database pdb1_database) {
        this.pdb1_database = pdb1_database;
    }
    public pdb1_Database getPdb1_database() {
        return pdb1_database;
    }

    public void setPdb1_database(pdb1_Database pdb1_database) {
        this.pdb1_database = pdb1_database;
    }

}