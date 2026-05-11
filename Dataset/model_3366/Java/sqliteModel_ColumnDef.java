





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_ColumnDef extends ColumnSource {

    private String type;





    private sqliteModel_InsertStatement sqlitemodel_insertstatement;


    public sqliteModel_ColumnDef(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public sqliteModel_InsertStatement getSqlitemodel_insertstatement() {
        return sqlitemodel_insertstatement;
    }

    public void setSqlitemodel_insertstatement(sqliteModel_InsertStatement sqlitemodel_insertstatement) {
        this.sqlitemodel_insertstatement = sqlitemodel_insertstatement;
    }

}