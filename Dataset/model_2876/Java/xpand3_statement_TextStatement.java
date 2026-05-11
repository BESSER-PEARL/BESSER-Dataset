





import java.util.List;
import java.util.ArrayList;

public class xpand3_statement_TextStatement extends AbstractStatement {

    private String value;
    private boolean deleteLine;



    public xpand3_statement_TextStatement(
        String value,        boolean deleteLine    ) {
        super(
        );
        this.value = value;
        this.deleteLine = deleteLine;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getDeleteline() {
        return deleteLine;
    }

    public void setDeleteline(boolean deleteLine) {
        this.deleteLine = deleteLine;
    }


}