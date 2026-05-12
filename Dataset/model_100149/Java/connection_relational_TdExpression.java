





import java.util.List;
import java.util.ArrayList;

public class connection_relational_TdExpression extends Expression {

    private String modificationDate;
    private String expressionVariableMap;
    private String name;
    private String version;



    public connection_relational_TdExpression(
        String modificationDate,        String expressionVariableMap,        String name,        String version    ) {
        super(
        );
        this.modificationDate = modificationDate;
        this.expressionVariableMap = expressionVariableMap;
        this.name = name;
        this.version = version;
    }


    public String getModificationdate() {
        return modificationDate;
    }

    public void setModificationdate(String modificationDate) {
        this.modificationDate = modificationDate;
    }
    public String getExpressionvariablemap() {
        return expressionVariableMap;
    }

    public void setExpressionvariablemap(String expressionVariableMap) {
        this.expressionVariableMap = expressionVariableMap;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}