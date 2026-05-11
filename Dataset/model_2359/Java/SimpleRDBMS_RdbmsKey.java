





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_RdbmsKey extends RdbmsModelElement {






    private SimpleRDBMS_RdbmsTable simplerdbms_rdbmstable;




    private SimpleRDBMS_RdbmsColumn simplerdbms_rdbmscolumn;




    private SimpleRDBMS_RdbmsTable simplerdbms_rdbmstable;




    private List<SimpleRDBMS_RdbmsColumn> simplerdbms_rdbmscolumns;


    public SimpleRDBMS_RdbmsKey(
    ) {
        super(
        );
        this.simplerdbms_rdbmscolumns = new ArrayList<>();
    }

    public SimpleRDBMS_RdbmsKey(
        ArrayList<SimpleRDBMS_RdbmsColumn> simplerdbms_rdbmscolumns    ) {
        this.simplerdbms_rdbmscolumns = simplerdbms_rdbmscolumns;
    }


    public SimpleRDBMS_RdbmsTable getSimplerdbms_rdbmstable() {
        return simplerdbms_rdbmstable;
    }

    public void setSimplerdbms_rdbmstable(SimpleRDBMS_RdbmsTable simplerdbms_rdbmstable) {
        this.simplerdbms_rdbmstable = simplerdbms_rdbmstable;
    }
    public SimpleRDBMS_RdbmsColumn getSimplerdbms_rdbmscolumn() {
        return simplerdbms_rdbmscolumn;
    }

    public void setSimplerdbms_rdbmscolumn(SimpleRDBMS_RdbmsColumn simplerdbms_rdbmscolumn) {
        this.simplerdbms_rdbmscolumn = simplerdbms_rdbmscolumn;
    }
    public SimpleRDBMS_RdbmsTable getSimplerdbms_rdbmstable() {
        return simplerdbms_rdbmstable;
    }

    public void setSimplerdbms_rdbmstable(SimpleRDBMS_RdbmsTable simplerdbms_rdbmstable) {
        this.simplerdbms_rdbmstable = simplerdbms_rdbmstable;
    }
    public List<SimpleRDBMS_RdbmsColumn> getSimplerdbms_rdbmscolumns() {
        return simplerdbms_rdbmscolumns;
    }

    public void addSimplerdbms_rdbmscolumn(Simplerdbms_rdbmscolumn simplerdbms_rdbmscolumn) {
        this.simplerdbms_rdbmscolumns.add(simplerdbms_rdbmscolumn);
    }

}