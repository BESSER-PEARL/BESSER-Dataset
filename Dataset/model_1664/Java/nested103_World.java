





import java.util.List;
import java.util.ArrayList;

public class nested103_World  {






    private List<nested103_EClass10> nested103_eclass10s;


    public nested103_World(
    ) {
        this.nested103_eclass10s = new ArrayList<>();
    }

    public nested103_World(
        ArrayList<nested103_EClass10> nested103_eclass10s    ) {
        this.nested103_eclass10s = nested103_eclass10s;
    }


    public List<nested103_EClass10> getNested103_eclass10s() {
        return nested103_eclass10s;
    }

    public void addNested103_eclass10(Nested103_eclass10 nested103_eclass10) {
        this.nested103_eclass10s.add(nested103_eclass10);
    }

}