





import java.util.List;
import java.util.ArrayList;

public class nested103_EClass1 extends NamedElement {






    private List<nested103_EClass2> nested103_eclass2s;




    private nested103_EClass0 nested103_eclass0;


    public nested103_EClass1(
    ) {
        super(
        );
        this.nested103_eclass2s = new ArrayList<>();
    }

    public nested103_EClass1(
        ArrayList<nested103_EClass2> nested103_eclass2s    ) {
        this.nested103_eclass2s = nested103_eclass2s;
    }


    public List<nested103_EClass2> getNested103_eclass2s() {
        return nested103_eclass2s;
    }

    public void addNested103_eclass2(Nested103_eclass2 nested103_eclass2) {
        this.nested103_eclass2s.add(nested103_eclass2);
    }
    public nested103_EClass0 getNested103_eclass0() {
        return nested103_eclass0;
    }

    public void setNested103_eclass0(nested103_EClass0 nested103_eclass0) {
        this.nested103_eclass0 = nested103_eclass0;
    }

}