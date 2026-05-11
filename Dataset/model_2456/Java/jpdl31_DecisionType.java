





import java.util.List;
import java.util.ArrayList;

public class jpdl31_DecisionType  {

    private String name;
    private String expression;
    private String group;
    private String async_;



    public jpdl31_DecisionType(
        String name,        String expression,        String group,        String async_    ) {
        this.name = name;
        this.expression = expression;
        this.group = group;
        this.async_ = async_;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getAsync_() {
        return async_;
    }

    public void setAsync_(String async_) {
        this.async_ = async_;
    }


}