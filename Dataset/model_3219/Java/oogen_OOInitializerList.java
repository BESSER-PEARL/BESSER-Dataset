





import java.util.List;
import java.util.ArrayList;

public class oogen_OOInitializerList extends OOExpression {






    private List<oogen_OOExpression> oogen_ooexpressions;


    public oogen_OOInitializerList(
    ) {
        super(
        );
        this.oogen_ooexpressions = new ArrayList<>();
    }

    public oogen_OOInitializerList(
        ArrayList<oogen_OOExpression> oogen_ooexpressions    ) {
        this.oogen_ooexpressions = oogen_ooexpressions;
    }


    public List<oogen_OOExpression> getOogen_ooexpressions() {
        return oogen_ooexpressions;
    }

    public void addOogen_ooexpression(Oogen_ooexpression oogen_ooexpression) {
        this.oogen_ooexpressions.add(oogen_ooexpression);
    }

}