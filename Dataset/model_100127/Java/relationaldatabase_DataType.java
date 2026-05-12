





import java.util.List;
import java.util.ArrayList;

public class relationaldatabase_DataType extends NamedElement {






    private relationaldatabase_Column relationaldatabase_column;




    private relationaldatabase_DatabaseModel relationaldatabase_databasemodel;


    public relationaldatabase_DataType(
    ) {
        super(
        );
    }



    public relationaldatabase_Column getRelationaldatabase_column() {
        return relationaldatabase_column;
    }

    public void setRelationaldatabase_column(relationaldatabase_Column relationaldatabase_column) {
        this.relationaldatabase_column = relationaldatabase_column;
    }
    public relationaldatabase_DatabaseModel getRelationaldatabase_databasemodel() {
        return relationaldatabase_databasemodel;
    }

    public void setRelationaldatabase_databasemodel(relationaldatabase_DatabaseModel relationaldatabase_databasemodel) {
        this.relationaldatabase_databasemodel = relationaldatabase_databasemodel;
    }

}