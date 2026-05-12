





import java.util.List;
import java.util.ArrayList;

public class XHTML_Tfoot extends Attrs, Cellhalign, Cellvalign {






    private List<Tr> trs;


    public XHTML_Tfoot(
    ) {
        super(
        );
        this.trs = new ArrayList<>();
    }

    public XHTML_Tfoot(
        ArrayList<Tr> trs    ) {
        this.trs = trs;
    }


    public List<Tr> getTrs() {
        return trs;
    }

    public void addTr(Tr tr) {
        this.trs.add(tr);
    }

}