





import java.util.List;
import java.util.ArrayList;

public class fiacre_Transition  {

    private String name;





    private fiacre_ProcessDecl fiacre_processdecl;




    private fiacre_Statement fiacre_statement;




    private fiacre_State fiacre_state;


    public fiacre_Transition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fiacre_ProcessDecl getFiacre_processdecl() {
        return fiacre_processdecl;
    }

    public void setFiacre_processdecl(fiacre_ProcessDecl fiacre_processdecl) {
        this.fiacre_processdecl = fiacre_processdecl;
    }
    public fiacre_Statement getFiacre_statement() {
        return fiacre_statement;
    }

    public void setFiacre_statement(fiacre_Statement fiacre_statement) {
        this.fiacre_statement = fiacre_statement;
    }
    public fiacre_State getFiacre_state() {
        return fiacre_state;
    }

    public void setFiacre_state(fiacre_State fiacre_state) {
        this.fiacre_state = fiacre_state;
    }

}