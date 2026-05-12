





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private String firstName;
    private String lastNAme;
    private String middleNAme;
    private String ID;
    private String socialsecurity;



    public Student(
        String firstName,        String lastNAme,        String middleNAme,        String ID,        String socialsecurity    ) {
        this.firstName = firstName;
        this.lastNAme = lastNAme;
        this.middleNAme = middleNAme;
        this.ID = ID;
        this.socialsecurity = socialsecurity;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getLastname() {
        return lastNAme;
    }

    public void setLastname(String lastNAme) {
        this.lastNAme = lastNAme;
    }
    public String getMiddlename() {
        return middleNAme;
    }

    public void setMiddlename(String middleNAme) {
        this.middleNAme = middleNAme;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getSocialsecurity() {
        return socialsecurity;
    }

    public void setSocialsecurity(String socialsecurity) {
        this.socialsecurity = socialsecurity;
    }


}