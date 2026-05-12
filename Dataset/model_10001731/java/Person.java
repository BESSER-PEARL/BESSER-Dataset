





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private int LibraryID;
    private int PersonID;
    private String BirthDay;
    private String PersonName;



    public Person(
        int LibraryID,        int PersonID,        String BirthDay,        String PersonName    ) {
        this.LibraryID = LibraryID;
        this.PersonID = PersonID;
        this.BirthDay = BirthDay;
        this.PersonName = PersonName;
    }


    public int getLibraryid() {
        return LibraryID;
    }

    public void setLibraryid(int LibraryID) {
        this.LibraryID = LibraryID;
    }
    public int getPersonid() {
        return PersonID;
    }

    public void setPersonid(int PersonID) {
        this.PersonID = PersonID;
    }
    public String getBirthday() {
        return BirthDay;
    }

    public void setBirthday(String BirthDay) {
        this.BirthDay = BirthDay;
    }
    public String getPersonname() {
        return PersonName;
    }

    public void setPersonname(String PersonName) {
        this.PersonName = PersonName;
    }


}