





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_RdbmsSchema extends RdbmsModelElement {






    private SimpleRDBMS_RdbmsTable simplerdbms_rdbmstable;




    private List<SimpleRDBMS_RdbmsTable> simplerdbms_rdbmstables;


    public SimpleRDBMS_RdbmsSchema(
    ) {
        super(
        );
        this.simplerdbms_rdbmstables = new ArrayList<>();
    }

    public SimpleRDBMS_RdbmsSchema(
        ArrayList<SimpleRDBMS_RdbmsTable> simplerdbms_rdbmstables    ) {
        this.simplerdbms_rdbmstables = simplerdbms_rdbmstables;
    }


    public SimpleRDBMS_RdbmsTable getSimplerdbms_rdbmstable() {
        return simplerdbms_rdbmstable;
    }

    public void setSimplerdbms_rdbmstable(SimpleRDBMS_RdbmsTable simplerdbms_rdbmstable) {
        this.simplerdbms_rdbmstable = simplerdbms_rdbmstable;
    }
    public List<SimpleRDBMS_RdbmsTable> getSimplerdbms_rdbmstables() {
        return simplerdbms_rdbmstables;
    }

    public void addSimplerdbms_rdbmstable(Simplerdbms_rdbmstable simplerdbms_rdbmstable) {
        this.simplerdbms_rdbmstables.add(simplerdbms_rdbmstable);
    }

}