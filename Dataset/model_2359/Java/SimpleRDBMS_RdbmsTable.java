





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_RdbmsTable extends RdbmsModelElement {






    private SimpleRDBMS_RdbmsColumn simplerdbms_rdbmscolumn;




    private List<SimpleRDBMS_RdbmsColumn> simplerdbms_rdbmscolumns;


    public SimpleRDBMS_RdbmsTable(
    ) {
        super(
        );
        this.simplerdbms_rdbmscolumns = new ArrayList<>();
    }

    public SimpleRDBMS_RdbmsTable(
        ArrayList<SimpleRDBMS_RdbmsColumn> simplerdbms_rdbmscolumns    ) {
        this.simplerdbms_rdbmscolumns = simplerdbms_rdbmscolumns;
    }


    public SimpleRDBMS_RdbmsColumn getSimplerdbms_rdbmscolumn() {
        return simplerdbms_rdbmscolumn;
    }

    public void setSimplerdbms_rdbmscolumn(SimpleRDBMS_RdbmsColumn simplerdbms_rdbmscolumn) {
        this.simplerdbms_rdbmscolumn = simplerdbms_rdbmscolumn;
    }
    public List<SimpleRDBMS_RdbmsColumn> getSimplerdbms_rdbmscolumns() {
        return simplerdbms_rdbmscolumns;
    }

    public void addSimplerdbms_rdbmscolumn(Simplerdbms_rdbmscolumn simplerdbms_rdbmscolumn) {
        this.simplerdbms_rdbmscolumns.add(simplerdbms_rdbmscolumn);
    }

}