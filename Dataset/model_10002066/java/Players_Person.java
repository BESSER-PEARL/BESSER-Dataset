





import java.util.List;
import java.util.ArrayList;

public class Players_Person  {

    private String personNumber;
    private String name;



    public Players_Person(
        String personNumber,        String name    ) {
        this.personNumber = personNumber;
        this.name = name;
    }


    public String getPersonnumber() {
        return personNumber;
    }

    public void setPersonnumber(String personNumber) {
        this.personNumber = personNumber;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}