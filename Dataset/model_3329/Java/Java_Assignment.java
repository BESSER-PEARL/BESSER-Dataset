





import java.util.List;
import java.util.ArrayList;

public class Java_Assignment extends Statement {

    private String variableExpr;
    private String objectId;
    private String fieldName;



    public Java_Assignment(
        String variableExpr,        String objectId,        String fieldName    ) {
        super(
        );
        this.variableExpr = variableExpr;
        this.objectId = objectId;
        this.fieldName = fieldName;
    }


    public String getVariableexpr() {
        return variableExpr;
    }

    public void setVariableexpr(String variableExpr) {
        this.variableExpr = variableExpr;
    }
    public String getObjectid() {
        return objectId;
    }

    public void setObjectid(String objectId) {
        this.objectId = objectId;
    }
    public String getFieldname() {
        return fieldName;
    }

    public void setFieldname(String fieldName) {
        this.fieldName = fieldName;
    }


}