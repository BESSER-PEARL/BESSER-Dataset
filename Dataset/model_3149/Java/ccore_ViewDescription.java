





import java.util.List;
import java.util.ArrayList;

public class ccore_ViewDescription  {






    private List<ccore_TypeDefinition> ccore_typedefinitions;


    public ccore_ViewDescription(
    ) {
        this.ccore_typedefinitions = new ArrayList<>();
    }

    public ccore_ViewDescription(
        ArrayList<ccore_TypeDefinition> ccore_typedefinitions    ) {
        this.ccore_typedefinitions = ccore_typedefinitions;
    }


    public List<ccore_TypeDefinition> getCcore_typedefinitions() {
        return ccore_typedefinitions;
    }

    public void addCcore_typedefinition(Ccore_typedefinition ccore_typedefinition) {
        this.ccore_typedefinitions.add(ccore_typedefinition);
    }

}