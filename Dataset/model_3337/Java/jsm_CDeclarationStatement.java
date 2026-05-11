





import java.util.List;
import java.util.ArrayList;

public class jsm_CDeclarationStatement extends AbstractCStatement, AbstractMTypeWithNameDeclaration {

    private boolean final;



    public jsm_CDeclarationStatement(
        boolean final    ) {
        super(
        );
        this.final = final;
    }


    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }


}