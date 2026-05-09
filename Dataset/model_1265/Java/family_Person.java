





import java.util.List;
import java.util.ArrayList;

public class family_Person  {

    private boolean male;
    private String name;





    private family_Family family_family;


    public family_Person(
        boolean male,        String name    ) {
        this.male = male;
        this.name = name;
    }


    public boolean getMale() {
        return male;
    }

    public void setMale(boolean male) {
        this.male = male;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public family_Family getFamily_family() {
        return family_family;
    }

    public void setFamily_family(family_Family family_family) {
        this.family_family = family_family;
    }

}