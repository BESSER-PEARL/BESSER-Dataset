





import java.util.List;
import java.util.ArrayList;

public class vhdl_statement_ExitStatement extends Statement {

    private String exit;



    public vhdl_statement_ExitStatement(
        String exit    ) {
        super(
        );
        this.exit = exit;
    }


    public String getExit() {
        return exit;
    }

    public void setExit(String exit) {
        this.exit = exit;
    }


}