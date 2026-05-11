





import java.util.List;
import java.util.ArrayList;

public class asmeta_basictransitionrules_MacroCallRule extends BasicRule {

    private String parameters;





    private basictransitionrules_MacroDeclaration basictransitionrules_macrodeclaration;


    public asmeta_basictransitionrules_MacroCallRule(
        String parameters    ) {
        super(
        );
        this.parameters = parameters;
    }


    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }

    public basictransitionrules_MacroDeclaration getBasictransitionrules_macrodeclaration() {
        return basictransitionrules_macrodeclaration;
    }

    public void setBasictransitionrules_macrodeclaration(basictransitionrules_MacroDeclaration basictransitionrules_macrodeclaration) {
        this.basictransitionrules_macrodeclaration = basictransitionrules_macrodeclaration;
    }

}