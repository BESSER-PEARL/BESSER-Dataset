





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_RdbmsTable extends RdbmsModelElement {






    private List<SimpleRDBMS_RdbmsForeignKey> simplerdbms_rdbmsforeignkeys;




    private List<SimpleRDBMS_RdbmsColumn> simplerdbms_rdbmscolumns;




    private SimpleRDBMS_RdbmsSchema simplerdbms_rdbmsschema;




    private SimpleRDBMS_RdbmsColumn simplerdbms_rdbmscolumn;




    private SimpleRDBMS_RdbmsForeignKey simplerdbms_rdbmsforeignkey;




    private SimpleRDBMS_RdbmsSchema simplerdbms_rdbmsschema;


    public SimpleRDBMS_RdbmsTable(
    ) {
        super(
        );
        this.simplerdbms_rdbmsforeignkeys = new ArrayList<>();
        this.simplerdbms_rdbmscolumns = new ArrayList<>();
    }

    public SimpleRDBMS_RdbmsTable(
        ArrayList<SimpleRDBMS_RdbmsForeignKey> simplerdbms_rdbmsforeignkeys,        ArrayList<SimpleRDBMS_RdbmsColumn> simplerdbms_rdbmscolumns    ) {
        this.simplerdbms_rdbmsforeignkeys = simplerdbms_rdbmsforeignkeys;
        this.simplerdbms_rdbmscolumns = simplerdbms_rdbmscolumns;
    }


    public List<SimpleRDBMS_RdbmsForeignKey> getSimplerdbms_rdbmsforeignkeys() {
        return simplerdbms_rdbmsforeignkeys;
    }

    public void addSimplerdbms_rdbmsforeignkey(Simplerdbms_rdbmsforeignkey simplerdbms_rdbmsforeignkey) {
        this.simplerdbms_rdbmsforeignkeys.add(simplerdbms_rdbmsforeignkey);
    }
    public List<SimpleRDBMS_RdbmsColumn> getSimplerdbms_rdbmscolumns() {
        return simplerdbms_rdbmscolumns;
    }

    public void addSimplerdbms_rdbmscolumn(Simplerdbms_rdbmscolumn simplerdbms_rdbmscolumn) {
        this.simplerdbms_rdbmscolumns.add(simplerdbms_rdbmscolumn);
    }
    public SimpleRDBMS_RdbmsSchema getSimplerdbms_rdbmsschema() {
        return simplerdbms_rdbmsschema;
    }

    public void setSimplerdbms_rdbmsschema(SimpleRDBMS_RdbmsSchema simplerdbms_rdbmsschema) {
        this.simplerdbms_rdbmsschema = simplerdbms_rdbmsschema;
    }
    public SimpleRDBMS_RdbmsColumn getSimplerdbms_rdbmscolumn() {
        return simplerdbms_rdbmscolumn;
    }

    public void setSimplerdbms_rdbmscolumn(SimpleRDBMS_RdbmsColumn simplerdbms_rdbmscolumn) {
        this.simplerdbms_rdbmscolumn = simplerdbms_rdbmscolumn;
    }
    public SimpleRDBMS_RdbmsForeignKey getSimplerdbms_rdbmsforeignkey() {
        return simplerdbms_rdbmsforeignkey;
    }

    public void setSimplerdbms_rdbmsforeignkey(SimpleRDBMS_RdbmsForeignKey simplerdbms_rdbmsforeignkey) {
        this.simplerdbms_rdbmsforeignkey = simplerdbms_rdbmsforeignkey;
    }
    public SimpleRDBMS_RdbmsSchema getSimplerdbms_rdbmsschema() {
        return simplerdbms_rdbmsschema;
    }

    public void setSimplerdbms_rdbmsschema(SimpleRDBMS_RdbmsSchema simplerdbms_rdbmsschema) {
        this.simplerdbms_rdbmsschema = simplerdbms_rdbmsschema;
    }

}