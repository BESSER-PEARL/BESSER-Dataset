





import java.util.List;
import java.util.ArrayList;

public class gastm_VirtualSpecification extends MinorSyntaxObject {






    private gastm_FunctionMemberAttributes gastm_functionmemberattributes;




    private gastm_DerivesFrom gastm_derivesfrom;


    public gastm_VirtualSpecification(
    ) {
        super(
        );
    }



    public gastm_FunctionMemberAttributes getGastm_functionmemberattributes() {
        return gastm_functionmemberattributes;
    }

    public void setGastm_functionmemberattributes(gastm_FunctionMemberAttributes gastm_functionmemberattributes) {
        this.gastm_functionmemberattributes = gastm_functionmemberattributes;
    }
    public gastm_DerivesFrom getGastm_derivesfrom() {
        return gastm_derivesfrom;
    }

    public void setGastm_derivesfrom(gastm_DerivesFrom gastm_derivesfrom) {
        this.gastm_derivesfrom = gastm_derivesfrom;
    }

}