





import java.util.List;
import java.util.ArrayList;

public class xpand3_declaration_Definition extends AbstractNamedDeclaration {






    private List<AbstractStatement> abstractstatements;


    public xpand3_declaration_Definition(
    ) {
        super(
        );
        this.abstractstatements = new ArrayList<>();
    }

    public xpand3_declaration_Definition(
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