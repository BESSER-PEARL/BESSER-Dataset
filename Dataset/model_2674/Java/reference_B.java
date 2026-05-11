





import java.util.List;
import java.util.ArrayList;

public class reference_B extends Named {






    private reference_A reference_a;




    private List<reference_C> reference_cs;


    public reference_B(
    ) {
        super(
        );
        this.reference_cs = new ArrayList<>();
    }

    public reference_B(
        ArrayList<reference_C> reference_cs    ) {
        this.reference_cs = reference_cs;
    }


    public reference_A getReference_a() {
        return reference_a;
    }

    public void setReference_a(reference_A reference_a) {
        this.reference_a = reference_a;
    }
    public List<reference_C> getReference_cs() {
        return reference_cs;
    }

    public void addReference_c(Reference_c reference_c) {
        this.reference_cs.add(reference_c);
    }

}