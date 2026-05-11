





import java.util.List;
import java.util.ArrayList;

public class containment_E extends Named {






    private List<containment_F> containment_fs;




    private containment_A containment_a;


    public containment_E(
    ) {
        super(
        );
        this.containment_fs = new ArrayList<>();
    }

    public containment_E(
        ArrayList<containment_F> containment_fs    ) {
        this.containment_fs = containment_fs;
    }


    public List<containment_F> getContainment_fs() {
        return containment_fs;
    }

    public void addContainment_f(Containment_f containment_f) {
        this.containment_fs.add(containment_f);
    }
    public containment_A getContainment_a() {
        return containment_a;
    }

    public void setContainment_a(containment_A containment_a) {
        this.containment_a = containment_a;
    }

}