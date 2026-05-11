





import java.util.List;
import java.util.ArrayList;

public class whileCpp_Command  {

    private String nop;





    private whileCpp_Vars whilecpp_vars;




    private whileCpp_Commands whilecpp_commands;


    public whileCpp_Command(
        String nop    ) {
        this.nop = nop;
    }


    public String getNop() {
        return nop;
    }

    public void setNop(String nop) {
        this.nop = nop;
    }

    public whileCpp_Vars getWhilecpp_vars() {
        return whilecpp_vars;
    }

    public void setWhilecpp_vars(whileCpp_Vars whilecpp_vars) {
        this.whilecpp_vars = whilecpp_vars;
    }
    public whileCpp_Commands getWhilecpp_commands() {
        return whilecpp_commands;
    }

    public void setWhilecpp_commands(whileCpp_Commands whilecpp_commands) {
        this.whilecpp_commands = whilecpp_commands;
    }

}