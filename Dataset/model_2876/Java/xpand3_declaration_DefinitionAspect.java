





import java.util.List;
import java.util.ArrayList;

public class xpand3_declaration_DefinitionAspect extends AbstractAspect {






    private List<AbstractStatement> abstractstatements;


    public xpand3_declaration_DefinitionAspect(
    ) {
        super(
        );
        this.abstractstatements = new ArrayList<>();
    }

    public xpand3_declaration_DefinitionAspect(
        ArrayList<AbstractStatement> abstractstatements    ) {
        this.abstractstatements = abstractstatements;
    }


    public List<AbstractStatement> getAbstractstatements() {
        return abstractstatements;
    }

    public void addAbstractstatement(Abstractstatement abstractstatement) {
        this.abstractstatements.add(abstractstatement);
    }

}