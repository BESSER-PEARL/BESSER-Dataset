





import java.util.List;
import java.util.ArrayList;

public class robochart_Variable extends NamedExpression, Member, TypedNamedElement {

    private String modifier;





    private robochart_VarRef robochart_varref;




    private robochart_SetComp robochart_setcomp;


    public robochart_Variable(
        String modifier    ) {
        super(
        );
        this.modifier = modifier;
    }


    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }

    public robochart_VarRef getRobochart_varref() {
        return robochart_varref;
    }

    public void setRobochart_varref(robochart_VarRef robochart_varref) {
        this.robochart_varref = robochart_varref;
    }
    public robochart_SetComp getRobochart_setcomp() {
        return robochart_setcomp;
    }

    public void setRobochart_setcomp(robochart_SetComp robochart_setcomp) {
        this.robochart_setcomp = robochart_setcomp;
    }

}