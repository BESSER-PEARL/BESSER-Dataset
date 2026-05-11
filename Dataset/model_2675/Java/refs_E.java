





import java.util.List;
import java.util.ArrayList;

public class refs_E extends Named {






    private refs_A refs_a;




    private List<refs_F> refs_fs;


    public refs_E(
    ) {
        super(
        );
        this.refs_fs = new ArrayList<>();
    }

    public refs_E(
        ArrayList<refs_F> refs_fs    ) {
        this.refs_fs = refs_fs;
    }


    public refs_A getRefs_a() {
        return refs_a;
    }

    public void setRefs_a(refs_A refs_a) {
        this.refs_a = refs_a;
    }
    public List<refs_F> getRefs_fs() {
        return refs_fs;
    }

    public void addRefs_f(Refs_f refs_f) {
        this.refs_fs.add(refs_f);
    }

}