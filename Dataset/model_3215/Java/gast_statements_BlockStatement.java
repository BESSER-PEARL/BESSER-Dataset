





import java.util.List;
import java.util.ArrayList;

public class gast_statements_BlockStatement extends Statement {

    private boolean synchronized;



    public gast_statements_BlockStatement(
        boolean synchronized    ) {
        super(
        );
        this.synchronized = synchronized;
    }


    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }


}