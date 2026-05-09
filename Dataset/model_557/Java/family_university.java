





import java.util.List;
import java.util.ArrayList;

public class family_university  {

    private String name;





    private family_person family_person;


    public family_university(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public family_person getFamily_person() {
        return family_person;
    }

    public void setFamily_person(family_person family_person) {
        this.family_person = family_person;
    }

}