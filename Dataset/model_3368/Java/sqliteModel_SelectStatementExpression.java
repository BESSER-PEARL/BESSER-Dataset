





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_SelectStatementExpression extends Expression {

    private boolean exists;
    private boolean not_;





    private sqliteModel_SelectStatement sqlitemodel_selectstatement;


    public sqliteModel_SelectStatementExpression(
        boolean exists,        boolean not_    ) {
        super(
        );
        this.exists = exists;
        this.not_ = not_;
    }


    public boolean getExists() {
        return exists;
    }

    public void setExists(boolean exists) {
        this.exists = exists;
    }
    public boolean getNot_() {
        return not_;
    }

    public void setNot_(boolean not_) {
        this.not_ = not_;
    }

    public sqliteModel_SelectStatement getSqlitemodel_selectstatement() {
        return sqlitemodel_selectstatement;
    }

    public void setSqlitemodel_selectstatement(sqliteModel_SelectStatement sqlitemodel_selectstatement) {
        this.sqlitemodel_selectstatement = sqlitemodel_selectstatement;
    }

}