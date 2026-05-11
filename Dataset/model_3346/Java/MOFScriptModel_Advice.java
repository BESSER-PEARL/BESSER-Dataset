





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_Advice extends MOFScriptStatementOwner {

    private String name;
    private String operator;
    private String pointCutRef;
    private String code;



    public MOFScriptModel_Advice(
        String name,        String operator,        String pointCutRef,        String code    ) {
        super(
        );
        this.name = name;
        this.operator = operator;
        this.pointCutRef = pointCutRef;
        this.code = code;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public String getPointcutref() {
        return pointCutRef;
    }

    public void setPointcutref(String pointCutRef) {
        this.pointCutRef = pointCutRef;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }


}