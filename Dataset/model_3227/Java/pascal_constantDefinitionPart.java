





import java.util.List;
import java.util.ArrayList;

public class pascal_constantDefinitionPart  {






    private List<pascal_constantDefinition> pascal_constantdefinitions;




    private pascal_block pascal_block;


    public pascal_constantDefinitionPart(
    ) {
        this.pascal_constantdefinitions = new ArrayList<>();
    }

    public pascal_constantDefinitionPart(
        ArrayList<pascal_constantDefinition> pascal_constantdefinitions    ) {
        this.pascal_constantdefinitions = pascal_constantdefinitions;
    }


    public List<pascal_constantDefinition> getPascal_constantdefinitions() {
        return pascal_constantdefinitions;
    }

    public void addPascal_constantdefinition(Pascal_constantdefinition pascal_constantdefinition) {
        this.pascal_constantdefinitions.add(pascal_constantdefinition);
    }
    public pascal_block getPascal_block() {
        return pascal_block;
    }

    public void setPascal_block(pascal_block pascal_block) {
        this.pascal_block = pascal_block;
    }

}