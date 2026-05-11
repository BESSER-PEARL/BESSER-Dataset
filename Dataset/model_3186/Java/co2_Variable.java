





import java.util.List;
import java.util.ArrayList;

public class co2_Variable extends VariableDeclaration {






    private co2_ProcessDefinition co2_processdefinition;




    private co2_DelimitedProcess co2_delimitedprocess;


    public co2_Variable(
    ) {
        super(
        );
    }



    public co2_ProcessDefinition getCo2_processdefinition() {
        return co2_processdefinition;
    }

    public void setCo2_processdefinition(co2_ProcessDefinition co2_processdefinition) {
        this.co2_processdefinition = co2_processdefinition;
    }
    public co2_DelimitedProcess getCo2_delimitedprocess() {
        return co2_delimitedprocess;
    }

    public void setCo2_delimitedprocess(co2_DelimitedProcess co2_delimitedprocess) {
        this.co2_delimitedprocess = co2_delimitedprocess;
    }

}