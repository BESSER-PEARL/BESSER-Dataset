





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_JoinStatement  {

    private boolean cross;
    private boolean natural;
    private boolean outer;
    private boolean inner;
    private boolean left;





    private sqliteModel_JoinSource sqlitemodel_joinsource;




    private sqliteModel_Expression sqlitemodel_expression;




    private sqliteModel_SingleSource sqlitemodel_singlesource;


    public sqliteModel_JoinStatement(
        boolean cross,        boolean natural,        boolean outer,        boolean inner,        boolean left    ) {
        this.cross = cross;
        this.natural = natural;
        this.outer = outer;
        this.inner = inner;
        this.left = left;
    }


    public boolean getCross() {
        return cross;
    }

    public void setCross(boolean cross) {
        this.cross = cross;
    }
    public boolean getNatural() {
        return natural;
    }

    public void setNatural(boolean natural) {
        this.natural = natural;
    }
    public boolean getOuter() {
        return outer;
    }

    public void setOuter(boolean outer) {
        this.outer = outer;
    }
    public boolean getInner() {
        return inner;
    }

    public void setInner(boolean inner) {
        this.inner = inner;
    }
    public boolean getLeft() {
        return left;
    }

    public void setLeft(boolean left) {
        this.left = left;
    }

    public sqliteModel_JoinSource getSqlitemodel_joinsource() {
        return sqlitemodel_joinsource;
    }

    public void setSqlitemodel_joinsource(sqliteModel_JoinSource sqlitemodel_joinsource) {
        this.sqlitemodel_joinsource = sqlitemodel_joinsource;
    }
    public sqliteModel_Expression getSqlitemodel_expression() {
        return sqlitemodel_expression;
    }

    public void setSqlitemodel_expression(sqliteModel_Expression sqlitemodel_expression) {
        this.sqlitemodel_expression = sqlitemodel_expression;
    }
    public sqliteModel_SingleSource getSqlitemodel_singlesource() {
        return sqlitemodel_singlesource;
    }

    public void setSqlitemodel_singlesource(sqliteModel_SingleSource sqlitemodel_singlesource) {
        this.sqlitemodel_singlesource = sqlitemodel_singlesource;
    }

}