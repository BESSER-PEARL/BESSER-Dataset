





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_SelectExpression extends SelectCoreExpression {

    private boolean distinct;
    private boolean allColumns;
    private boolean all;



    public sqliteModel_SelectExpression(
        boolean distinct,        boolean allColumns,        boolean all    ) {
        super(
        );
        this.distinct = distinct;
        this.allColumns = allColumns;
        this.all = all;
    }


    public boolean getDistinct() {
        return distinct;
    }

    public void setDistinct(boolean distinct) {
        this.distinct = distinct;
    }
    public boolean getAllcolumns() {
        return allColumns;
    }

    public void setAllcolumns(boolean allColumns) {
        this.allColumns = allColumns;
    }
    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }


}