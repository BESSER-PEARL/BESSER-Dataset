





import java.util.List;
import java.util.ArrayList;

public class simplerdbms_Schema extends RModelElement {






    private simplerdbms_Table simplerdbms_table;




    private List<simplerdbms_Table> simplerdbms_tables;




    private simplerdbms_ForeignKey simplerdbms_foreignkey;


    public simplerdbms_Schema(
    ) {
        super(
        );
        this.simplerdbms_tables = new ArrayList<>();
    }

    public simplerdbms_Schema(
        ArrayList<simplerdbms_Table> simplerdbms_tables    ) {
        this.simplerdbms_tables = simplerdbms_tables;
    }


    public simplerdbms_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(simplerdbms_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
    }
    public List<simplerdbms_Table> getSimplerdbms_tables() {
        return simplerdbms_tables;
    }

    public void addSimplerdbms_table(Simplerdbms_table simplerdbms_table) {
        this.simplerdbms_tables.add(simplerdbms_table);
    }
    public simplerdbms_ForeignKey getSimplerdbms_foreignkey() {
        return simplerdbms_foreignkey;
    }

    public void setSimplerdbms_foreignkey(simplerdbms_ForeignKey simplerdbms_foreignkey) {
        this.simplerdbms_foreignkey = simplerdbms_foreignkey;
    }

}