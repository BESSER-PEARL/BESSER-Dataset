





import java.util.List;
import java.util.ArrayList;

public class family_Family  {






    private List<family_Father> family_fathers;


    public family_Family(
    ) {
        this.family_fathers = new ArrayList<>();
    }

    public family_Family(
        ArrayList<family_Father> family_fathers    ) {
        this.family_fathers = family_fathers;
    }


    public List<family_Father> getFamily_fathers() {
        return family_fathers;
    }

    public void addFamily_father(Family_father family_father) {
        this.family_fathers.add(family_father);
    }

}