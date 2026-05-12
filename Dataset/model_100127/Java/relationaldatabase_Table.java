





import java.util.List;
import java.util.ArrayList;

public class relationaldatabase_Table extends NamedElement {






    private relationaldatabase_DatabaseModel relationaldatabase_databasemodel;




    private List<relationaldatabase_Column> relationaldatabase_columns;


    public relationaldatabase_Table(
    ) {
        super(
        );
        this.relationaldatabase_columns = new ArrayList<>();
    }

    public relationaldatabase_Table(
        ArrayList<relationaldatabase_Column> relationaldatabase_columns    ) {
        this.relationaldatabase_columns = relationaldatabase_columns;
    }


    public relationaldatabase_DatabaseModel getRelationaldatabase_databasemodel() {
        return relationaldatabase_databasemodel;
    }

    public void setRelationaldatabase_databasemodel(relationaldatabase_DatabaseModel relationaldatabase_databasemodel) {
        this.relationaldatabase_databasemodel = relationaldatabase_databasemodel;
    }
    public List<relationaldatabase_Column> getRelationaldatabase_columns() {
        return relationaldatabase_columns;
    }

    public void addRelationaldatabase_column(Relationaldatabase_column relationaldatabase_column) {
        this.relationaldatabase_columns.add(relationaldatabase_column);
    }

}