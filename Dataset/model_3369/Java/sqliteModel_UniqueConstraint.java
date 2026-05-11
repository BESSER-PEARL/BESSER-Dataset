





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_UniqueConstraint extends ColumnConstraint {






    private sqliteModel_ConflictClause sqlitemodel_conflictclause;


    public sqliteModel_UniqueConstraint(
    ) {
        super(
        );
    }



    public sqliteModel_ConflictClause getSqlitemodel_conflictclause() {
        return sqlitemodel_conflictclause;
    }

    public void setSqlitemodel_conflictclause(sqliteModel_ConflictClause sqlitemodel_conflictclause) {
        this.sqlitemodel_conflictclause = sqlitemodel_conflictclause;
    }

}