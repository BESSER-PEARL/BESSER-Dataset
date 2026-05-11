





import java.util.List;
import java.util.ArrayList;

public class caltrop_StateVariable extends Variable {

    private boolean constant;





    private caltrop_CaltropActorImpl caltrop_caltropactorimpl;


    public caltrop_StateVariable(
        boolean constant    ) {
        super(
        );
        this.constant = constant;
    }


    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }

    public caltrop_CaltropActorImpl getCaltrop_caltropactorimpl() {
        return caltrop_caltropactorimpl;
    }

    public void setCaltrop_caltropactorimpl(caltrop_CaltropActorImpl caltrop_caltropactorimpl) {
        this.caltrop_caltropactorimpl = caltrop_caltropactorimpl;
    }

}