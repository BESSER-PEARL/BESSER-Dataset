





import java.util.List;
import java.util.ArrayList;

public class astm_VariableDeclaration extends Declaration {

    private boolean isMutable;



    public astm_VariableDeclaration(
        boolean isMutable    ) {
        super(
        );
        this.isMutable = isMutable;
    }


    public boolean getIsmutable() {
        return isMutable;
    }

    public void setIsmutable(boolean isMutable) {
        this.isMutable = isMutable;
    }


}