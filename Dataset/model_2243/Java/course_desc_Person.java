





import java.util.List;
import java.util.ArrayList;

public class course_desc_Person  {

    private String fullName;
    private String lastName;
    private String name;
    private String personNr;



    public course_desc_Person(
        String fullName,        String lastName,        String name,        String personNr    ) {
        this.fullName = fullName;
        this.lastName = lastName;
        this.name = name;
        this.personNr = personNr;
    }


    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPersonnr() {
        return personNr;
    }

    public void setPersonnr(String personNr) {
        this.personNr = personNr;
    }


}