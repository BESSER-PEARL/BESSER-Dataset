





import java.util.List;
import java.util.ArrayList;

public class semlink_A extends NamedElement {






    private semlink_G semlink_g;




    private List<semlink_B> semlink_bs;




    private semlink_B semlink_b;


    public semlink_A(
    ) {
        super(
        );
        this.semlink_bs = new ArrayList<>();
    }

    public semlink_A(
        ArrayList<semlink_B> semlink_bs    ) {
        this.semlink_bs = semlink_bs;
    }


    public semlink_G getSemlink_g() {
        return semlink_g;
    }

    public void setSemlink_g(semlink_G semlink_g) {
        this.semlink_g = semlink_g;
    }
    public List<semlink_B> getSemlink_bs() {
        return semlink_bs;
    }

    public void addSemlink_b(Semlink_b semlink_b) {
        this.semlink_bs.add(semlink_b);
    }
    public semlink_B getSemlink_b() {
        return semlink_b;
    }

    public void setSemlink_b(semlink_B semlink_b) {
        this.semlink_b = semlink_b;
    }

}