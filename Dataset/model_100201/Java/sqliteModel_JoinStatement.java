





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_JoinStatement  {

    private boolean left;
    private boolean natural;
    private boolean inner;
    private boolean outer;
    private boolean cross;





    private sqliteModel_JoinSource sqlitemodel_joinsource;




    private sqliteModel_Expression sqlitemodel_expression;




    private sqliteModel_SingleSource sqlitemodel_singlesource;


    public sqliteModel_JoinStatement(
        boolean left,        boolean natural,        boolean inner,        boolean outer,        boolean cross    ) {
        this.left = left;
        this.natural = natural;
        this.inner = inner;
        this.outer = outer;
        this.cross = cross;
    }


    public boolean getLeft() {
        return left;
    }

    public void setLeft(boolean left) {
        this.left = left;
    }
    public boolean getNatural() {
        return natural;
    }

    public void setNatural(boolean natural) {
        this.natural = natural;
    }
    public boolean getInner() {
        return inner;
    }

    public void setInner(boolean inner) {
        this.inner = inner;
    }
    public boolean getOuter() {
        return outer;
    }

    public void setOuter(boolean outer) {
        this.outer = outer;
    }
    public boolean getCross() {
        return cross;
    }

    public void setCross(boolean cross) {
        this.cross = cross;
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