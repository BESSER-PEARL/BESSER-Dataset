





import java.util.List;
import java.util.ArrayList;

public class model_requirements_CEGNode extends IModelNode {

    private String variable;
    private String condition;
    private String type;



    public model_requirements_CEGNode(
        String variable,        String condition,        String type    ) {
        super(
        );
        this.variable = variable;
        this.condition = condition;
        this.type = type;
    }


    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }
    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}