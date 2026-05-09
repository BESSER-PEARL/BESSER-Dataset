





import java.util.List;
import java.util.ArrayList;

public class ast_Identifier extends Expression {

    private String quotedValue;
    private String value;
    private String escapedValue;





    private ast_BehaviorFeature ast_behaviorfeature;


    public ast_Identifier(
        String quotedValue,        String value,        String escapedValue    ) {
        super(
        );
        this.quotedValue = quotedValue;
        this.value = value;
        this.escapedValue = escapedValue;
    }


    public String getQuotedvalue() {
        return quotedValue;
    }

    public void setQuotedvalue(String quotedValue) {
        this.quotedValue = quotedValue;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getEscapedvalue() {
        return escapedValue;
    }

    public void setEscapedvalue(String escapedValue) {
        this.escapedValue = escapedValue;
    }

    public ast_BehaviorFeature getAst_behaviorfeature() {
        return ast_behaviorfeature;
    }

    public void setAst_behaviorfeature(ast_BehaviorFeature ast_behaviorfeature) {
        this.ast_behaviorfeature = ast_behaviorfeature;
    }

}