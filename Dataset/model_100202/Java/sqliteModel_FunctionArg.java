





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_FunctionArg  {

    private String type;
    private String name;





    private sqliteModel_Function sqlitemodel_function;




    private sqliteModel_FunctionArgument sqlitemodel_functionargument;


    public sqliteModel_FunctionArg(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sqliteModel_Function getSqlitemodel_function() {
        return sqlitemodel_function;
    }

    public void setSqlitemodel_function(sqliteModel_Function sqlitemodel_function) {
        this.sqlitemodel_function = sqlitemodel_function;
    }
    public sqliteModel_FunctionArgument getSqlitemodel_functionargument() {
        return sqlitemodel_functionargument;
    }

    public void setSqlitemodel_functionargument(sqliteModel_FunctionArgument sqlitemodel_functionargument) {
        this.sqlitemodel_functionargument = sqlitemodel_functionargument;
    }

}