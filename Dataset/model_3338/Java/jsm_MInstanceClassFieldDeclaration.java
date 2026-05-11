





import java.util.List;
import java.util.ArrayList;

public class jsm_MInstanceClassFieldDeclaration extends AbstractMClassFieldDeclaration {

    private boolean transient;



    public jsm_MInstanceClassFieldDeclaration(
        boolean transient    ) {
        super(
        );
        this.transient = transient;
    }


    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }


}