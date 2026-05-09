





import java.util.List;
import java.util.ArrayList;

public class astm_RDBTableSpaceDefinition extends Definition {






    private List<astm_NameSpaceDefinition> astm_namespacedefinitions;


    public astm_RDBTableSpaceDefinition(
    ) {
        super(
        );
        this.astm_namespacedefinitions = new ArrayList<>();
    }

    public astm_RDBTableSpaceDefinition(
        ArrayList<astm_NameSpaceDefinition> astm_namespacedefinitions    ) {
        this.astm_namespacedefinitions = astm_namespacedefinitions;
    }


    public List<astm_NameSpaceDefinition> getAstm_namespacedefinitions() {
        return astm_namespacedefinitions;
    }

    public void addAstm_namespacedefinition(Astm_namespacedefinition astm_namespacedefinition) {
        this.astm_namespacedefinitions.add(astm_namespacedefinition);
    }

}