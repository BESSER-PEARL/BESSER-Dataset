





import java.util.List;
import java.util.ArrayList;

public class simpleRdbms_Table extends RModelElement {






    private List<simpleRdbms_Column> simplerdbms_columns;




    private simpleRdbms_Schema simplerdbms_schema;




    private simpleRdbms_Column simplerdbms_column;




    private simpleRdbms_Schema simplerdbms_schema;


    public simpleRdbms_Table(
    ) {
        super(
        );
        this.simplerdbms_columns = new ArrayList<>();
    }

    public simpleRdbms_Table(
        ArrayList<simpleRdbms_Column> simplerdbms_columns    ) {
        this.simplerdbms_columns = simplerdbms_columns;
    }


    public List<simpleRdbms_Column> getSimplerdbms_columns() {
        return simplerdbms_columns;
    }

    public void addSimplerdbms_column(Simplerdbms_column simplerdbms_column) {
        this.simplerdbms_columns.add(simplerdbms_column);
    }
    public simpleRdbms_Schema getSimplerdbms_schema() {
        return simplerdbms_schema;
    }

    public void setSimplerdbms_schema(simpleRdbms_Schema simplerdbms_schema) {
        this.simplerdbms_schema = simplerdbms_schema;
    }
    public simpleRdbms_Column getSimplerdbms_column() {
        return simplerdbms_column;
    }

    public void setSimplerdbms_column(simpleRdbms_Column simplerdbms_column) {
        this.simplerdbms_column = simplerdbms_column;
    }
    public simpleRdbms_Schema getSimplerdbms_schema() {
        return simplerdbms_schema;
    }

    public void setSimplerdbms_schema(simpleRdbms_Schema simplerdbms_schema) {
        this.simplerdbms_schema = simplerdbms_schema;
    }

}