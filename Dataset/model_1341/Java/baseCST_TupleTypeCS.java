





import java.util.List;
import java.util.ArrayList;

public class baseCST_TupleTypeCS extends TypedRefCS, Nameable {

    private String name;





    private List<baseCST_TuplePartCS> basecst_tuplepartcss;


    public baseCST_TupleTypeCS(
        String name    ) {
        super(
        );
        this.name = name;
        this.basecst_tuplepartcss = new ArrayList<>();
    }

    public baseCST_TupleTypeCS(
        String name        ArrayList<baseCST_TuplePartCS> basecst_tuplepartcss    ) {
        this.name = name;
        this.basecst_tuplepartcss = basecst_tuplepartcss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<baseCST_TuplePartCS> getBasecst_tuplepartcss() {
        return basecst_tuplepartcss;
    }

    public void addBasecst_tuplepartcs(Basecst_tuplepartcs basecst_tuplepartcs) {
        this.basecst_tuplepartcss.add(basecst_tuplepartcs);
    }

}