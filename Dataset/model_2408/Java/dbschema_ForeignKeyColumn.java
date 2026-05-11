





import java.util.List;
import java.util.ArrayList;

public class dbschema_ForeignKeyColumn extends Column {






    private dbschema_AttributeColumn dbschema_attributecolumn;


    public dbschema_ForeignKeyColumn(
    ) {
        super(
        );
    }



    public dbschema_AttributeColumn getDbschema_attributecolumn() {
        return dbschema_attributecolumn;
    }

    public void setDbschema_attributecolumn(dbschema_AttributeColumn dbschema_attributecolumn) {
        this.dbschema_attributecolumn = dbschema_attributecolumn;
    }

}