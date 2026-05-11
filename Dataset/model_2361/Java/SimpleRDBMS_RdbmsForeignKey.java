





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_RdbmsForeignKey extends RdbmsModelElement {






    private List<SimpleRDBMS_RdbmsColumn> simplerdbms_rdbmscolumns;




    private SimpleRDBMS_RdbmsColumn simplerdbms_rdbmscolumn;


    public SimpleRDBMS_RdbmsForeignKey(
    ) {
        super(
        );
        this.simplerdbms_rdbmscolumns = new ArrayList<>();
    }

    public SimpleRDBMS_RdbmsForeignKey(
        ArrayList<SimpleRDBMS_RdbmsColumn> simplerdbms_rdbmscolumns    ) {
        this.simplerdbms_rdbmscolumns = simplerdbms_rdbmscolumns;
    }


    public List<SimpleRDBMS_RdbmsColumn> getSimplerdbms_rdbmscolumns() {
        return simplerdbms_rdbmscolumns;
    }

    public void addSimplerdbms_rdbmscolumn(Simplerdbms_rdbmscolumn simplerdbms_rdbmscolumn) {
        this.simplerdbms_rdbmscolumns.add(simplerdbms_rdbmscolumn);
    }
    public SimpleRDBMS_RdbmsColumn getSimplerdbms_rdbmscolumn() {
        return simplerdbms_rdbmscolumn;
    }

    public void setSimplerdbms_rdbmscolumn(SimpleRDBMS_RdbmsColumn simplerdbms_rdbmscolumn) {
        this.simplerdbms_rdbmscolumn = simplerdbms_rdbmscolumn;
    }

}