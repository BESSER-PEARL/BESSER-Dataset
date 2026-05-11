





import java.util.List;
import java.util.ArrayList;

public class refs_G extends Named {






    private refs_B refs_b;




    private refs_A refs_a;




    private List<refs_H> refs_hs;


    public refs_G(
    ) {
        super(
        );
        this.refs_hs = new ArrayList<>();
    }

    public refs_G(
        ArrayList<refs_H> refs_hs    ) {
        this.refs_hs = refs_hs;
    }


    public refs_B getRefs_b() {
        return refs_b;
    }

    public void setRefs_b(refs_B refs_b) {
        this.refs_b = refs_b;
    }
    public refs_A getRefs_a() {
        return refs_a;
    }

    public void setRefs_a(refs_A refs_a) {
        this.refs_a = refs_a;
    }
    public List<refs_H> getRefs_hs() {
        return refs_hs;
    }

    public void addRefs_h(Refs_h refs_h) {
        this.refs_hs.add(refs_h);
    }

}