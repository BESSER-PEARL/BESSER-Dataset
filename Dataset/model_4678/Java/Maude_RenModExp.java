





import java.util.List;
import java.util.ArrayList;

public class Maude_RenModExp extends ModExpression {






    private Maude_ModExpression maude_modexpression;




    private List<Maude_RenMapping> maude_renmappings;


    public Maude_RenModExp(
    ) {
        super(
        );
        this.maude_renmappings = new ArrayList<>();
    }

    public Maude_RenModExp(
        ArrayList<Maude_RenMapping> maude_renmappings    ) {
        this.maude_renmappings = maude_renmappings;
    }


    public Maude_ModExpression getMaude_modexpression() {
        return maude_modexpression;
    }

    public void setMaude_modexpression(Maude_ModExpression maude_modexpression) {
        this.maude_modexpression = maude_modexpression;
    }
    public List<Maude_RenMapping> getMaude_renmappings() {
        return maude_renmappings;
    }

    public void addMaude_renmapping(Maude_renmapping maude_renmapping) {
        this.maude_renmappings.add(maude_renmapping);
    }

}