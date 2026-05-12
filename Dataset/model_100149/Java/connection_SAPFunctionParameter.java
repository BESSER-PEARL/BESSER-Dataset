





import java.util.List;
import java.util.ArrayList;

public class connection_SAPFunctionParameter  {

    private String name;
    private boolean changing;
    private String description;
    private String testValue;
    private String type;
    private boolean tableResideInTables;
    private String length;





    private connection_SAPFunctionParamData connection_sapfunctionparamdata;




    private connection_SAPFunctionParameter connection_sapfunctionparameter;




    private connection_SAPFunctionParamData connection_sapfunctionparamdata;


    public connection_SAPFunctionParameter(
        String name,        boolean changing,        String description,        String testValue,        String type,        boolean tableResideInTables,        String length    ) {
        this.name = name;
        this.changing = changing;
        this.description = description;
        this.testValue = testValue;
        this.type = type;
        this.tableResideInTables = tableResideInTables;
        this.length = length;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getChanging() {
        return changing;
    }

    public void setChanging(boolean changing) {
        this.changing = changing;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getTestvalue() {
        return testValue;
    }

    public void setTestvalue(String testValue) {
        this.testValue = testValue;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getTableresideintables() {
        return tableResideInTables;
    }

    public void setTableresideintables(boolean tableResideInTables) {
        this.tableResideInTables = tableResideInTables;
    }
    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }

    public connection_SAPFunctionParamData getConnection_sapfunctionparamdata() {
        return connection_sapfunctionparamdata;
    }

    public void setConnection_sapfunctionparamdata(connection_SAPFunctionParamData connection_sapfunctionparamdata) {
        this.connection_sapfunctionparamdata = connection_sapfunctionparamdata;
    }
    public connection_SAPFunctionParameter getConnection_sapfunctionparameter() {
        return connection_sapfunctionparameter;
    }

    public void setConnection_sapfunctionparameter(connection_SAPFunctionParameter connection_sapfunctionparameter) {
        this.connection_sapfunctionparameter = connection_sapfunctionparameter;
    }
    public connection_SAPFunctionParamData getConnection_sapfunctionparamdata() {
        return connection_sapfunctionparamdata;
    }

    public void setConnection_sapfunctionparamdata(connection_SAPFunctionParamData connection_sapfunctionparamdata) {
        this.connection_sapfunctionparamdata = connection_sapfunctionparamdata;
    }

}