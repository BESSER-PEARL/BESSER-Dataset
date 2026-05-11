





import java.util.List;
import java.util.ArrayList;

public class pdb2_Person  {

    private String id;
    private String incrementalID;
    private String placeOfBirth;
    private String name;
    private String birthday;





    private pdb2_Database pdb2_database;




    private pdb2_Database pdb2_database;


    public pdb2_Person(
        String id,        String incrementalID,        String placeOfBirth,        String name,        String birthday    ) {
        this.id = id;
        this.incrementalID = incrementalID;
        this.placeOfBirth = placeOfBirth;
        this.name = name;
        this.birthday = birthday;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBirthday() {
        return birthday;
    }

    public void setBirthday(String birthday) {
        this.birthday = birthday;
    }

    public pdb2_Database getPdb2_database() {
        return pdb2_database;
    }

    public void setPdb2_database(pdb2_Database pdb2_database) {
        this.pdb2_database = pdb2_database;
    }
    public pdb2_Database getPdb2_database() {
        return pdb2_database;
    }

    public void setPdb2_database(pdb2_Database pdb2_database) {
        this.pdb2_database = pdb2_database;
    }

}