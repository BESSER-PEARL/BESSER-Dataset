





import java.util.List;
import java.util.ArrayList;

public class jpdl32_DecisionType  {

    private String name;
    private String group;
    private String description;
    private String expression;
    private String async_;



    public jpdl32_DecisionType(
        String name,        String group,        String description,        String expression,        String async_    ) {
        this.name = name;
        this.group = group;
        this.description = description;
        this.expression = expression;
        this.async_ = async_;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getAsync_() {
        return async_;
    }

    public void setAsync_(String async_) {
        this.async_ = async_;
    }


}