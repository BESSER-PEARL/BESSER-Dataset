





import java.util.List;
import java.util.ArrayList;

public class syntax_ddl_CallStatement extends DefinitionStatement {

    private String parms;



    public syntax_ddl_CallStatement(
        String parms    ) {
        super(
        );
        this.parms = parms;
    }


    public String getParms() {
        return parms;
    }

    public void setParms(String parms) {
        this.parms = parms;
    }


}