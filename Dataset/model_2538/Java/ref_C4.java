





import java.util.List;
import java.util.ArrayList;

public class ref_C4  {






    private ref_D ref_d;




    private ref_C ref_c;




    private List<ref_D> ref_ds;




    private ref_C ref_c;


    public ref_C4(
    ) {
        this.ref_ds = new ArrayList<>();
    }

    public ref_C4(
        ArrayList<ref_D> ref_ds    ) {
        this.ref_ds = ref_ds;
    }


    public ref_D getRef_d() {
        return ref_d;
    }

    public void setRef_d(ref_D ref_d) {
        this.ref_d = ref_d;
    }
    public ref_C getRef_c() {
        return ref_c;
    }

    public void setRef_c(ref_C ref_c) {
        this.ref_c = ref_c;
    }
    public List<ref_D> getRef_ds() {
        return ref_ds;
    }

    public void addRef_d(Ref_d ref_d) {
        this.ref_ds.add(ref_d);
    }
    public ref_C getRef_c() {
        return ref_c;
    }

    public void setRef_c(ref_C ref_c) {
        this.ref_c = ref_c;
    }

}