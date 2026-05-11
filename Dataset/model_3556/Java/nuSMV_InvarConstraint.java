





import java.util.List;
import java.util.ArrayList;

public class nuSMV_InvarConstraint extends ModuleElement {

    private boolean semicolon;



    public nuSMV_InvarConstraint(
        boolean semicolon    ) {
        super(
        );
        this.semicolon = semicolon;
    }


    public boolean getSemicolon() {
        return semicolon;
    }

    public void setSemicolon(boolean semicolon) {
        this.semicolon = semicolon;
    }


}