





import java.util.List;
import java.util.ArrayList;

public class JDTAST_Type extends ASTNode {






    private JDTAST_TypeParameter jdtast_typeparameter;




    private JDTAST_MethodRefParameter jdtast_methodrefparameter;


    public JDTAST_Type(
    ) {
        super(
        );
    }



    public JDTAST_TypeParameter getJdtast_typeparameter() {
        return jdtast_typeparameter;
    }

    public void setJdtast_typeparameter(JDTAST_TypeParameter jdtast_typeparameter) {
        this.jdtast_typeparameter = jdtast_typeparameter;
    }
    public JDTAST_MethodRefParameter getJdtast_methodrefparameter() {
        return jdtast_methodrefparameter;
    }

    public void setJdtast_methodrefparameter(JDTAST_MethodRefParameter jdtast_methodrefparameter) {
        this.jdtast_methodrefparameter = jdtast_methodrefparameter;
    }

}