





import java.util.List;
import java.util.ArrayList;

public class cobol_statements_Exit extends Statement {

    private String exitLabel;



    public cobol_statements_Exit(
        String exitLabel    ) {
        super(
        );
        this.exitLabel = exitLabel;
    }


    public String getExitlabel() {
        return exitLabel;
    }

    public void setExitlabel(String exitLabel) {
        this.exitLabel = exitLabel;
    }


}