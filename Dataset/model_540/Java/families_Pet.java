





import java.util.List;
import java.util.ArrayList;

public class families_Pet extends NamedElement {

    private boolean male;





    private families_Family families_family;


    public families_Pet(
        boolean male    ) {
        super(
        );
        this.male = male;
    }


    public boolean getMale() {
        return male;
    }

    public void setMale(boolean male) {
        this.male = male;
    }

    public families_Family getFamilies_family() {
        return families_family;
    }

    public void setFamilies_family(families_Family families_family) {
        this.families_family = families_family;
    }

}