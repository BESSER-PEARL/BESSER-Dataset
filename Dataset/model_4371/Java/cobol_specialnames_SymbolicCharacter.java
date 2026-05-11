





import java.util.List;
import java.util.ArrayList;

public class cobol_specialnames_SymbolicCharacter extends SpecialName {






    private List<IntegerLiteral> integerliterals;


    public cobol_specialnames_SymbolicCharacter(
    ) {
        super(
        );
        this.integerliterals = new ArrayList<>();
    }

    public cobol_specialnames_SymbolicCharacter(
        ArrayList<IntegerLiteral> integerliterals    ) {
        this.integerliterals = integerliterals;
    }


    public List<IntegerLiteral> getIntegerliterals() {
        return integerliterals;
    }

    public void addIntegerliteral(Integerliteral integerliteral) {
        this.integerliterals.add(integerliteral);
    }

}