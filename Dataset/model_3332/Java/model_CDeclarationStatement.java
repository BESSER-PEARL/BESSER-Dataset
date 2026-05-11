





import java.util.List;
import java.util.ArrayList;

public class model_CDeclarationStatement extends AbstractMTypeWithNameDeclaration, AbstractCStatement {

    private boolean final;



    public model_CDeclarationStatement(
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