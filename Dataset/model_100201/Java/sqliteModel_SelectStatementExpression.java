





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_SelectStatementExpression extends Expression {

    private boolean not_;
    private boolean exists;





    private sqliteModel_SelectStatement sqlitemodel_selectstatement;


    public sqliteModel_SelectStatementExpression(
        boolean not_,        boolean exists    ) {
        super(
        );
        this.not_ = not_;
        this.exists = exists;
    }


    public boolean getNot_() {
        return not_;
    }

    public void setNot_(boolean not_) {
        this.not_ = not_;
    }
    public boolean getExists() {
        return exists;
    }

    public void setExists(boolean exists) {
        this.exists = exists;
    }

    public sqliteModel_SelectStatement getSqlitemodel_selectstatement() {
        return sqlitemodel_selectstatement;
    }

    public void setSqlitemodel_selectstatement(sqliteModel_SelectStatement sqlitemodel_selectstatement) {
        this.sqlitemodel_selectstatement = sqlitemodel_selectstatement;
    }

}