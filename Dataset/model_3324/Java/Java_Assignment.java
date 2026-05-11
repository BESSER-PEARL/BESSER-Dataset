





import java.util.List;
import java.util.ArrayList;

public class Java_Assignment extends Statement {

    private String objectId;
    private String variableExpr;
    private String fieldName;



    public Java_Assignment(
        String objectId,        String variableExpr,        String fieldName    ) {
        super(
        );
        this.objectId = objectId;
        this.variableExpr = variableExpr;
        this.fieldName = fieldName;
    }


    public String getObjectid() {
        return objectId;
    }

    public void setObjectid(String objectId) {
        this.objectId = objectId;
    }
    public String getVariableexpr() {
        return variableExpr;
    }

    public void setVariableexpr(String variableExpr) {
        this.variableExpr = variableExpr;
    }
    public String getFieldname() {
        return fieldName;
    }

    public void setFieldname(String fieldName) {
        this.fieldName = fieldName;
    }


}