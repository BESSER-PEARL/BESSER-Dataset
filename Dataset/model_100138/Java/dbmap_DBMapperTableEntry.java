





import java.util.List;
import java.util.ArrayList;

public class dbmap_DBMapperTableEntry  {

    private boolean join;
    private String operator;
    private String type;
    private String name;
    private boolean nullable;
    private String expression;





    private dbmap_AbstractDBDataMapTable dbmap_abstractdbdatamaptable;


    public dbmap_DBMapperTableEntry(
        boolean join,        String operator,        String type,        String name,        boolean nullable,        String expression    ) {
        this.join = join;
        this.operator = operator;
        this.type = type;
        this.name = name;
        this.nullable = nullable;
        this.expression = expression;
    }


    public boolean getJoin() {
        return join;
    }

    public void setJoin(boolean join) {
        this.join = join;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
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
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public dbmap_AbstractDBDataMapTable getDbmap_abstractdbdatamaptable() {
        return dbmap_abstractdbdatamaptable;
    }

    public void setDbmap_abstractdbdatamaptable(dbmap_AbstractDBDataMapTable dbmap_abstractdbdatamaptable) {
        this.dbmap_abstractdbdatamaptable = dbmap_abstractdbdatamaptable;
    }

}