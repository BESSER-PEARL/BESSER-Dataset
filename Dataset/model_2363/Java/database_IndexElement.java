





import java.util.List;
import java.util.ArrayList;

public class database_IndexElement extends DatabaseElement {

    private boolean asc;





    private database_Index database_index;




    private database_Column database_column;




    private database_Column database_column;


    public database_IndexElement(
        boolean asc    ) {
        super(
        );
        this.asc = asc;
    }


    public boolean getAsc() {
        return asc;
    }

    public void setAsc(boolean asc) {
        this.asc = asc;
    }

    public database_Index getDatabase_index() {
        return database_index;
    }

    public void setDatabase_index(database_Index database_index) {
        this.database_index = database_index;
    }
    public database_Column getDatabase_column() {
        return database_column;
    }

    public void setDatabase_column(database_Column database_column) {
        this.database_column = database_column;
    }
    public database_Column getDatabase_column() {
        return database_column;
    }

    public void setDatabase_column(database_Column database_column) {
        this.database_column = database_column;
    }

}