





import java.util.List;
import java.util.ArrayList;

public class family_Root  {






    private List<family_family> family_familys;


    public family_Root(
    ) {
        this.family_familys = new ArrayList<>();
    }

    public family_Root(
        ArrayList<family_family> family_familys    ) {
        this.family_familys = family_familys;
    }


    public List<family_family> getFamily_familys() {
        return family_familys;
    }

    public void addFamily_family(Family_family family_family) {
        this.family_familys.add(family_family);
    }

}