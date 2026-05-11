





import java.util.List;
import java.util.ArrayList;

public class cm_seff_ExternalCallAction extends AbstractAction {






    private Signature signature;




    private RequiredRole requiredrole;


    public cm_seff_ExternalCallAction(
    ) {
        super(
        );
    }



    public Signature getSignature() {
        return signature;
    }

    public void setSignature(Signature signature) {
        this.signature = signature;
    }
    public RequiredRole getRequiredrole() {
        return requiredrole;
    }

    public void setRequiredrole(RequiredRole requiredrole) {
        this.requiredrole = requiredrole;
    }

}