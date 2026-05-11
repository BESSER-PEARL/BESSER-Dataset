





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_RdbmsTable extends RdbmsModelElement {






    private List<SimpleRDBMS_RdbmsKey> simplerdbms_rdbmskeys;




    private SimpleRDBMS_RdbmsForeignKey simplerdbms_rdbmsforeignkey;




    private List<SimpleRDBMS_RdbmsColumn> simplerdbms_rdbmscolumns;




    private List<SimpleRDBMS_RdbmsForeignKey> simplerdbms_rdbmsforeignkeys;




    private SimpleRDBMS_RdbmsKey simplerdbms_rdbmskey;




    private SimpleRDBMS_RdbmsColumn simplerdbms_rdbmscolumn;


    public SimpleRDBMS_RdbmsTable(
    ) {
        super(
        );
        this.simplerdbms_rdbmskeys = new ArrayList<>();
        this.simplerdbms_rdbmscolumns = new ArrayList<>();
        this.simplerdbms_rdbmsforeignkeys = new ArrayList<>();
    }

    public SimpleRDBMS_RdbmsTable(
        ArrayList<SimpleRDBMS_RdbmsKey> simplerdbms_rdbmskeys,        ArrayList<SimpleRDBMS_RdbmsColumn> simplerdbms_rdbmscolumns,        ArrayList<SimpleRDBMS_RdbmsForeignKey> simplerdbms_rdbmsforeignkeys    ) {
        this.simplerdbms_rdbmskeys = simplerdbms_rdbmskeys;
        this.simplerdbms_rdbmscolumns = simplerdbms_rdbmscolumns;
        this.simplerdbms_rdbmsforeignkeys = simplerdbms_rdbmsforeignkeys;
    }


    public List<SimpleRDBMS_RdbmsKey> getSimplerdbms_rdbmskeys() {
        return simplerdbms_rdbmskeys;
    }

    public void addSimplerdbms_rdbmskey(Simplerdbms_rdbmskey simplerdbms_rdbmskey) {
        this.simplerdbms_rdbmskeys.add(simplerdbms_rdbmskey);
    }
    public SimpleRDBMS_RdbmsForeignKey getSimplerdbms_rdbmsforeignkey() {
        return simplerdbms_rdbmsforeignkey;
    }

    public void setSimplerdbms_rdbmsforeignkey(SimpleRDBMS_RdbmsForeignKey simplerdbms_rdbmsforeignkey) {
        this.simplerdbms_rdbmsforeignkey = simplerdbms_rdbmsforeignkey;
    }
    public List<SimpleRDBMS_RdbmsColumn> getSimplerdbms_rdbmscolumns() {
        return simplerdbms_rdbmscolumns;
    }

    public void addSimplerdbms_rdbmscolumn(Simplerdbms_rdbmscolumn simplerdbms_rdbmscolumn) {
        this.simplerdbms_rdbmscolumns.add(simplerdbms_rdbmscolumn);
    }
    public List<SimpleRDBMS_RdbmsForeignKey> getSimplerdbms_rdbmsforeignkeys() {
        return simplerdbms_rdbmsforeignkeys;
    }

    public void addSimplerdbms_rdbmsforeignkey(Simplerdbms_rdbmsforeignkey simplerdbms_rdbmsforeignkey) {
        this.simplerdbms_rdbmsforeignkeys.add(simplerdbms_rdbmsforeignkey);
    }
    public SimpleRDBMS_RdbmsKey getSimplerdbms_rdbmskey() {
        return simplerdbms_rdbmskey;
    }

    public void setSimplerdbms_rdbmskey(SimpleRDBMS_RdbmsKey simplerdbms_rdbmskey) {
        this.simplerdbms_rdbmskey = simplerdbms_rdbmskey;
    }
    public SimpleRDBMS_RdbmsColumn getSimplerdbms_rdbmscolumn() {
        return simplerdbms_rdbmscolumn;
    }

    public void setSimplerdbms_rdbmscolumn(SimpleRDBMS_RdbmsColumn simplerdbms_rdbmscolumn) {
        this.simplerdbms_rdbmscolumn = simplerdbms_rdbmscolumn;
    }

}