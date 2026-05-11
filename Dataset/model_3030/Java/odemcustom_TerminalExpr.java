





import java.util.List;
import java.util.ArrayList;

public class odemcustom_TerminalExpr extends RhsExpression {

    private String terminal;



    public odemcustom_TerminalExpr(
        String terminal    ) {
        super(
        );
        this.terminal = terminal;
    }


    public String getTerminal() {
        return terminal;
    }

    public void setTerminal(String terminal) {
        this.terminal = terminal;
    }


}