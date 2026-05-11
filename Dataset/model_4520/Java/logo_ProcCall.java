





import java.util.List;
import java.util.ArrayList;

public class logo_ProcCall extends Instruction {

    private int actualArgs;





    private logo_ProcDeclaration logo_procdeclaration;


    public logo_ProcCall(
        int actualArgs    ) {
        super(
        );
        this.actualArgs = actualArgs;
    }


    public int getActualargs() {
        return actualArgs;
    }

    public void setActualargs(int actualArgs) {
        this.actualArgs = actualArgs;
    }

    public logo_ProcDeclaration getLogo_procdeclaration() {
        return logo_procdeclaration;
    }

    public void setLogo_procdeclaration(logo_ProcDeclaration logo_procdeclaration) {
        this.logo_procdeclaration = logo_procdeclaration;
    }

}