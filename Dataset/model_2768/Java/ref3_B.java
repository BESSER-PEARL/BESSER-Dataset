





import java.util.List;
import java.util.ArrayList;

public class ref3_B extends Named {






    private List<ref3_D> ref3_ds;




    private ref3_N ref3_n;


    public ref3_B(
    ) {
        super(
        );
        this.ref3_ds = new ArrayList<>();
    }

    public ref3_B(
        ArrayList<ref3_D> ref3_ds    ) {
        this.ref3_ds = ref3_ds;
    }


    public List<ref3_D> getRef3_ds() {
        return ref3_ds;
    }

    public void addRef3_d(Ref3_d ref3_d) {
        this.ref3_ds.add(ref3_d);
    }
    public ref3_N getRef3_n() {
        return ref3_n;
    }

    public void setRef3_n(ref3_N ref3_n) {
        this.ref3_n = ref3_n;
    }

}