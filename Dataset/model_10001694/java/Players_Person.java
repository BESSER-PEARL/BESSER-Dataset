





import java.util.List;
import java.util.ArrayList;

public class Players_Person  {

    private String name;
    private String personNumber;



    public Players_Person(
        String name,        String personNumber    ) {
        this.name = name;
        this.personNumber = personNumber;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPersonnumber() {
        return personNumber;
    }

    public void setPersonnumber(String personNumber) {
        this.personNumber = personNumber;
    }


}