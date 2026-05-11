





import java.util.List;
import java.util.ArrayList;

public class Maude_ModImportation extends ModElement {

    private String mode;





    private Maude_ModExpression maude_modexpression;


    public Maude_ModImportation(
        String mode    ) {
        super(
        );
        this.mode = mode;
    }


    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public Maude_ModExpression getMaude_modexpression() {
        return maude_modexpression;
    }

    public void setMaude_modexpression(Maude_ModExpression maude_modexpression) {
        this.maude_modexpression = maude_modexpression;
    }

}