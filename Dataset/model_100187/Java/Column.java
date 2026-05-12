





import java.util.List;
import java.util.ArrayList;

public class Column  {






    private sql_schema_ColumnConstraint sql_schema_columnconstraint;




    private sql_schema_DefaultOption sql_schema_defaultoption;


    public Column(
    ) {
    }



    public sql_schema_ColumnConstraint getSql_schema_columnconstraint() {
        return sql_schema_columnconstraint;
    }

    public void setSql_schema_columnconstraint(sql_schema_ColumnConstraint sql_schema_columnconstraint) {
        this.sql_schema_columnconstraint = sql_schema_columnconstraint;
    }
    public sql_schema_DefaultOption getSql_schema_defaultoption() {
        return sql_schema_defaultoption;
    }

    public void setSql_schema_defaultoption(sql_schema_DefaultOption sql_schema_defaultoption) {
        this.sql_schema_defaultoption = sql_schema_defaultoption;
    }

}