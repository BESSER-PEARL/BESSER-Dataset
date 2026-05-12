





import java.util.List;
import java.util.ArrayList;

public class XHTML_Colgroup extends Attrs, Cellvalign, Cellhalign {






    private List<Col> cols;


    public XHTML_Colgroup(
    ) {
        super(
        );
        this.cols = new ArrayList<>();
    }

    public XHTML_Colgroup(
        ArrayList<Col> cols    ) {
        this.cols = cols;
    }


    public List<Col> getCols() {
        return cols;
    }

    public void addCol(Col col) {
        this.cols.add(col);
    }

}