





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_ReferenceClause  {






    private List<ddlDsl_Column> ddldsl_columns;




    private ddlDsl_Column ddldsl_column;




    private ddlDsl_CreateTable ddldsl_createtable;


    public ddlDsl_ReferenceClause(
    ) {
        this.ddldsl_columns = new ArrayList<>();
    }

    public ddlDsl_ReferenceClause(
        ArrayList<ddlDsl_Column> ddldsl_columns    ) {
        this.ddldsl_columns = ddldsl_columns;
    }


    public List<ddlDsl_Column> getDdldsl_columns() {
        return ddldsl_columns;
    }

    public void addDdldsl_column(Ddldsl_column ddldsl_column) {
        this.ddldsl_columns.add(ddldsl_column);
    }
    public ddlDsl_Column getDdldsl_column() {
        return ddldsl_column;
    }

    public void setDdldsl_column(ddlDsl_Column ddldsl_column) {
        this.ddldsl_column = ddldsl_column;
    }
    public ddlDsl_CreateTable getDdldsl_createtable() {
        return ddldsl_createtable;
    }

    public void setDdldsl_createtable(ddlDsl_CreateTable ddldsl_createtable) {
        this.ddldsl_createtable = ddldsl_createtable;
    }

}