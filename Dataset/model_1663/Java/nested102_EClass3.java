





import java.util.List;
import java.util.ArrayList;

public class nested102_EClass3 extends NamedElement {






    private List<nested102_EClass4> nested102_eclass4s;




    private nested102_EClass2 nested102_eclass2;


    public nested102_EClass3(
    ) {
        super(
        );
        this.nested102_eclass4s = new ArrayList<>();
    }

    public nested102_EClass3(
        ArrayList<nested102_EClass4> nested102_eclass4s    ) {
        this.nested102_eclass4s = nested102_eclass4s;
    }


    public List<nested102_EClass4> getNested102_eclass4s() {
        return nested102_eclass4s;
    }

    public void addNested102_eclass4(Nested102_eclass4 nested102_eclass4) {
        this.nested102_eclass4s.add(nested102_eclass4);
    }
    public nested102_EClass2 getNested102_eclass2() {
        return nested102_eclass2;
    }

    public void setNested102_eclass2(nested102_EClass2 nested102_eclass2) {
        this.nested102_eclass2 = nested102_eclass2;
    }

}