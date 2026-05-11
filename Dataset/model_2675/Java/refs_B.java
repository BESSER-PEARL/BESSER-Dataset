





import java.util.List;
import java.util.ArrayList;

public class refs_B extends Named {






    private refs_A refs_a;




    private List<refs_C> refs_cs;


    public refs_B(
    ) {
        super(
        );
        this.refs_cs = new ArrayList<>();
    }

    public refs_B(
        ArrayList<refs_C> refs_cs    ) {
        this.refs_cs = refs_cs;
    }


    public refs_A getRefs_a() {
        return refs_a;
    }

    public void setRefs_a(refs_A refs_a) {
        this.refs_a = refs_a;
    }
    public List<refs_C> getRefs_cs() {
        return refs_cs;
    }

    public void addRefs_c(Refs_c refs_c) {
        this.refs_cs.add(refs_c);
    }

}