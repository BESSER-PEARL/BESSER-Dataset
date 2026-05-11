





import java.util.List;
import java.util.ArrayList;

public class reference_E extends Named {






    private reference_A reference_a;




    private List<reference_F> reference_fs;


    public reference_E(
    ) {
        super(
        );
        this.reference_fs = new ArrayList<>();
    }

    public reference_E(
        ArrayList<reference_F> reference_fs    ) {
        this.reference_fs = reference_fs;
    }


    public reference_A getReference_a() {
        return reference_a;
    }

    public void setReference_a(reference_A reference_a) {
        this.reference_a = reference_a;
    }
    public List<reference_F> getReference_fs() {
        return reference_fs;
    }

    public void addReference_f(Reference_f reference_f) {
        this.reference_fs.add(reference_f);
    }

}