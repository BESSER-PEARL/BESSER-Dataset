





import java.util.List;
import java.util.ArrayList;

public class asmeta_structure_Body  {






    private List<RuleDeclaration> ruledeclarations;


    public asmeta_structure_Body(
    ) {
        this.ruledeclarations = new ArrayList<>();
    }

    public asmeta_structure_Body(
        ArrayList<RuleDeclaration> ruledeclarations    ) {
        this.ruledeclarations = ruledeclarations;
    }


    public List<RuleDeclaration> getRuledeclarations() {
        return ruledeclarations;
    }

    public void addRuledeclaration(Ruledeclaration ruledeclaration) {
        this.ruledeclarations.add(ruledeclaration);
    }

}