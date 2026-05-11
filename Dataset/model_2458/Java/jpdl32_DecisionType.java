





import java.util.List;
import java.util.ArrayList;

public class jpdl32_DecisionType  {

    private String expression;
    private String group;
    private String description;
    private String async_;
    private String name;



    public jpdl32_DecisionType(
        String expression,        String group,        String description,        String async_,        String name    ) {
        this.expression = expression;
        this.group = group;
        this.description = description;
        this.async_ = async_;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getAsync_() {
        return async_;
    }

    public void setAsync_(String async_) {
        this.async_ = async_;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}