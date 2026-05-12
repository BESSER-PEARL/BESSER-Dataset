





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_Schema extends RModelElement {






    private SimpleRDBMS_Table simplerdbms_table;




    private List<SimpleRDBMS_Table> simplerdbms_tables;


    public SimpleRDBMS_Schema(
    ) {
        super(
        );
        this.simplerdbms_tables = new ArrayList<>();
    }

    public SimpleRDBMS_Schema(
        ArrayList<SimpleRDBMS_Table> simplerdbms_tables    ) {
        this.simplerdbms_tables = simplerdbms_tables;
    }


    public SimpleRDBMS_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(SimpleRDBMS_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
    }
    public List<SimpleRDBMS_Table> getSimplerdbms_tables() {
        return simplerdbms_tables;
    }

    public void addSimplerdbms_table(Simplerdbms_table simplerdbms_table) {
        this.simplerdbms_tables.add(simplerdbms_table);
    }

}