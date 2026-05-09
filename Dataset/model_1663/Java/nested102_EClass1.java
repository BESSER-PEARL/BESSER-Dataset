





import java.util.List;
import java.util.ArrayList;

public class nested102_EClass1 extends NamedElement {






    private List<nested102_EClass2> nested102_eclass2s;




    private nested102_EClass0 nested102_eclass0;


    public nested102_EClass1(
    ) {
        super(
        );
        this.nested102_eclass2s = new ArrayList<>();
    }

    public nested102_EClass1(
        ArrayList<nested102_EClass2> nested102_eclass2s    ) {
        this.nested102_eclass2s = nested102_eclass2s;
    }


    public List<nested102_EClass2> getNested102_eclass2s() {
        return nested102_eclass2s;
    }

    public void addNested102_eclass2(Nested102_eclass2 nested102_eclass2) {
        this.nested102_eclass2s.add(nested102_eclass2);
    }
    public nested102_EClass0 getNested102_eclass0() {
        return nested102_eclass0;
    }

    public void setNested102_eclass0(nested102_EClass0 nested102_eclass0) {
        this.nested102_eclass0 = nested102_eclass0;
    }

}