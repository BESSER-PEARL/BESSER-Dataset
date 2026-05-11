





import java.util.List;
import java.util.ArrayList;

public class ref_C1  {






    private ref_A ref_a;




    private List<ref_B> ref_bs;


    public ref_C1(
    ) {
        this.ref_bs = new ArrayList<>();
    }

    public ref_C1(
        ArrayList<ref_B> ref_bs    ) {
        this.ref_bs = ref_bs;
    }


    public ref_A getRef_a() {
        return ref_a;
    }

    public void setRef_a(ref_A ref_a) {
        this.ref_a = ref_a;
    }
    public List<ref_B> getRef_bs() {
        return ref_bs;
    }

    public void addRef_b(Ref_b ref_b) {
        this.ref_bs.add(ref_b);
    }

}