





import java.util.List;
import java.util.ArrayList;

public class nested103_EClass3 extends NamedElement {






    private List<nested103_EClass4> nested103_eclass4s;




    private nested103_EClass2 nested103_eclass2;


    public nested103_EClass3(
    ) {
        super(
        );
        this.nested103_eclass4s = new ArrayList<>();
    }

    public nested103_EClass3(
        ArrayList<nested103_EClass4> nested103_eclass4s    ) {
        this.nested103_eclass4s = nested103_eclass4s;
    }


    public List<nested103_EClass4> getNested103_eclass4s() {
        return nested103_eclass4s;
    }

    public void addNested103_eclass4(Nested103_eclass4 nested103_eclass4) {
        this.nested103_eclass4s.add(nested103_eclass4);
    }
    public nested103_EClass2 getNested103_eclass2() {
        return nested103_eclass2;
    }

    public void setNested103_eclass2(nested103_EClass2 nested103_eclass2) {
        this.nested103_eclass2 = nested103_eclass2;
    }

}