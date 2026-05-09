





import java.util.List;
import java.util.ArrayList;

public class sastm_RDBSelectExpression extends Expression {






    private List<NameSpaceDefinition> namespacedefinitions;




    private List<IncludeUnit> includeunits;


    public sastm_RDBSelectExpression(
    ) {
        super(
        );
        this.namespacedefinitions = new ArrayList<>();
        this.includeunits = new ArrayList<>();
    }

    public sastm_RDBSelectExpression(
        ArrayList<NameSpaceDefinition> namespacedefinitions,        ArrayList<IncludeUnit> includeunits    ) {
        this.namespacedefinitions = namespacedefinitions;
        this.includeunits = includeunits;
    }


    public List<NameSpaceDefinition> getNamespacedefinitions() {
        return namespacedefinitions;
    }

    public void addNamespacedefinition(Namespacedefinition namespacedefinition) {
        this.namespacedefinitions.add(namespacedefinition);
    }
    public List<IncludeUnit> getIncludeunits() {
        return includeunits;
    }

    public void addIncludeunit(Includeunit includeunit) {
        this.includeunits.add(includeunit);
    }

}