





import java.util.List;
import java.util.ArrayList;

public class v125case5_B extends Named {






    private List<v125case5_D> v125case5_ds;




    private v125case5_N v125case5_n;


    public v125case5_B(
    ) {
        super(
        );
        this.v125case5_ds = new ArrayList<>();
    }

    public v125case5_B(
        ArrayList<v125case5_D> v125case5_ds    ) {
        this.v125case5_ds = v125case5_ds;
    }


    public List<v125case5_D> getV125case5_ds() {
        return v125case5_ds;
    }

    public void addV125case5_d(V125case5_d v125case5_d) {
        this.v125case5_ds.add(v125case5_d);
    }
    public v125case5_N getV125case5_n() {
        return v125case5_n;
    }

    public void setV125case5_n(v125case5_N v125case5_n) {
        this.v125case5_n = v125case5_n;
    }

}