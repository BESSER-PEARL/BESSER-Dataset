





import java.util.List;
import java.util.ArrayList;

public class XHTML_Thead extends Attrs, Cellvalign, Cellhalign {






    private List<Tr> trs;


    public XHTML_Thead(
    ) {
        super(
        );
        this.trs = new ArrayList<>();
    }

    public XHTML_Thead(
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