





import java.util.List;
import java.util.ArrayList;

public class nested102_EClass4 extends NamedElement {






    private List<nested102_EClass5> nested102_eclass5s;


    public nested102_EClass4(
    ) {
        super(
        );
        this.nested102_eclass5s = new ArrayList<>();
    }

    public nested102_EClass4(
        ArrayList<nested102_EClass5> nested102_eclass5s    ) {
        this.nested102_eclass5s = nested102_eclass5s;
    }


    public List<nested102_EClass5> getNested102_eclass5s() {
        return nested102_eclass5s;
    }

    public void addNested102_eclass5(Nested102_eclass5 nested102_eclass5) {
        this.nested102_eclass5s.add(nested102_eclass5);
    }

}