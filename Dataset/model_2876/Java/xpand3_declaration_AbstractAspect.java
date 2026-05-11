





import java.util.List;
import java.util.ArrayList;

public class xpand3_declaration_AbstractAspect extends AbstractDeclaration {

    private boolean wildparams;



    public xpand3_declaration_AbstractAspect(
        boolean wildparams    ) {
        super(
        );
        this.wildparams = wildparams;
    }


    public boolean getWildparams() {
        return wildparams;
    }

    public void setWildparams(boolean wildparams) {
        this.wildparams = wildparams;
    }


}