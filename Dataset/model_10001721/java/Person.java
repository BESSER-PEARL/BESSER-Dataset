





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String BirthDate;
    private int ID;
    private String Gender;
    private String FullName;
    private String AccessLevel;



    public Person(
        String BirthDate,        int ID,        String Gender,        String FullName,        String AccessLevel    ) {
        this.BirthDate = BirthDate;
        this.ID = ID;
        this.Gender = Gender;
        this.FullName = FullName;
        this.AccessLevel = AccessLevel;
    }


    public String getBirthdate() {
        return BirthDate;
    }

    public void setBirthdate(String BirthDate) {
        this.BirthDate = BirthDate;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }
    public String getFullname() {
        return FullName;
    }

    public void setFullname(String FullName) {
        this.FullName = FullName;
    }
    public String getAccesslevel() {
        return AccessLevel;
    }

    public void setAccesslevel(String AccessLevel) {
        this.AccessLevel = AccessLevel;
    }


}