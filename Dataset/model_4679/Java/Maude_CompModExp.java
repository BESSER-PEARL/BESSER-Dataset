





import java.util.List;
import java.util.ArrayList;

public class Maude_CompModExp extends ModExpression {






    private List<Maude_ModExpression> maude_modexpressions;


    public Maude_CompModExp(
    ) {
        super(
        );
        this.maude_modexpressions = new ArrayList<>();
    }

    public Maude_CompModExp(
        ArrayList<Maude_ModExpression> maude_modexpressions    ) {
        this.maude_modexpressions = maude_modexpressions;
    }


    public List<Maude_ModExpression> getMaude_modexpressions() {
        return maude_modexpressions;
    }

    public void addMaude_modexpression(Maude_modexpression maude_modexpression) {
        this.maude_modexpressions.add(maude_modexpression);
    }

}