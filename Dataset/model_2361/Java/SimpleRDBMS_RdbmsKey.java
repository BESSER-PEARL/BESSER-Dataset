





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_RdbmsKey extends RdbmsModelElement {






    private SimpleRDBMS_RdbmsForeignKey simplerdbms_rdbmsforeignkey;




    private SimpleRDBMS_RdbmsColumn simplerdbms_rdbmscolumn;




    private List<SimpleRDBMS_RdbmsForeignKey> simplerdbms_rdbmsforeignkeys;




    private List<SimpleRDBMS_RdbmsColumn> simplerdbms_rdbmscolumns;


    public SimpleRDBMS_RdbmsKey(
    ) {
        super(
        );
        this.simplerdbms_rdbmsforeignkeys = new ArrayList<>();
        this.simplerdbms_rdbmscolumns = new ArrayList<>();
    }

    public SimpleRDBMS_RdbmsKey(
        ArrayList<SimpleRDBMS_RdbmsForeignKey> simplerdbms_rdbmsforeignkeys,        ArrayList<SimpleRDBMS_RdbmsColumn> simplerdbms_rdbmscolumns    ) {
        this.simplerdbms_rdbmsforeignkeys = simplerdbms_rdbmsforeignkeys;
        this.simplerdbms_rdbmscolumns = simplerdbms_rdbmscolumns;
    }


    public SimpleRDBMS_RdbmsForeignKey getSimplerdbms_rdbmsforeignkey() {
        return simplerdbms_rdbmsforeignkey;
    }

    public void setSimplerdbms_rdbmsforeignkey(SimpleRDBMS_RdbmsForeignKey simplerdbms_rdbmsforeignkey) {
        this.simplerdbms_rdbmsforeignkey = simplerdbms_rdbmsforeignkey;
    }
    public SimpleRDBMS_RdbmsColumn getSimplerdbms_rdbmscolumn() {
        return simplerdbms_rdbmscolumn;
    }

    public void setSimplerdbms_rdbmscolumn(SimpleRDBMS_RdbmsColumn simplerdbms_rdbmscolumn) {
        this.simplerdbms_rdbmscolumn = simplerdbms_rdbmscolumn;
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

}