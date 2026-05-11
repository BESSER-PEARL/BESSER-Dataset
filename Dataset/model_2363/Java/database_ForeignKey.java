





import java.util.List;
import java.util.ArrayList;

public class database_ForeignKey extends NamedElement {






    private database_Column database_column;


    public database_ForeignKey(
    ) {
        super(
        );
    }



    public database_Column getDatabase_column() {
        return database_column;
    }

    public void setDatabase_column(database_Column database_column) {
        this.database_column = database_column;
    }

}