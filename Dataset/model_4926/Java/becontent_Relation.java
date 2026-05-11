





import java.util.List;
import java.util.ArrayList;

public class becontent_Relation extends DefinitionItem {

    private String name;
    private String variableName;



    public becontent_Relation(
        String name,        String variableName    ) {
        super(
        );
        this.name = name;
        this.variableName = variableName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }


}