





import java.util.List;
import java.util.ArrayList;

public class library_Parameter extends Base {

    private String description;
    private String value;
    private String expressionName;
    private String modifiable;
    private String name;



    public library_Parameter(
        String description,        String value,        String expressionName,        String modifiable,        String name    ) {
        super(
        );
        this.description = description;
        this.value = value;
        this.expressionName = expressionName;
        this.modifiable = modifiable;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getExpressionname() {
        return expressionName;
    }

    public void setExpressionname(String expressionName) {
        this.expressionName = expressionName;
    }
    public String getModifiable() {
        return modifiable;
    }

    public void setModifiable(String modifiable) {
        this.modifiable = modifiable;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}