





import java.util.List;
import java.util.ArrayList;

public class reference_G extends Named {






    private reference_A reference_a;




    private reference_B reference_b;




    private List<reference_H> reference_hs;


    public reference_G(
    ) {
        super(
        );
        this.reference_hs = new ArrayList<>();
    }

    public reference_G(
        ArrayList<reference_H> reference_hs    ) {
        this.reference_hs = reference_hs;
    }


    public reference_A getReference_a() {
        return reference_a;
    }

    public void setReference_a(reference_A reference_a) {
        this.reference_a = reference_a;
    }
    public reference_B getReference_b() {
        return reference_b;
    }

    public void setReference_b(reference_B reference_b) {
        this.reference_b = reference_b;
    }
    public List<reference_H> getReference_hs() {
        return reference_hs;
    }

    public void addReference_h(Reference_h reference_h) {
        this.reference_hs.add(reference_h);
    }

}