





import java.util.List;
import java.util.ArrayList;

public class dbschema_AttributeColumn extends Column {






    private dbschema_ForeignKeyColumn dbschema_foreignkeycolumn;


    public dbschema_AttributeColumn(
    ) {
        super(
        );
    }



    public dbschema_ForeignKeyColumn getDbschema_foreignkeycolumn() {
        return dbschema_foreignkeycolumn;
    }

    public void setDbschema_foreignkeycolumn(dbschema_ForeignKeyColumn dbschema_foreignkeycolumn) {
        this.dbschema_foreignkeycolumn = dbschema_foreignkeycolumn;
    }

}