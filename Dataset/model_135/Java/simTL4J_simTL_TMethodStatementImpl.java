





import java.util.List;
import java.util.ArrayList;

public class simTL4J_simTL_TMethodStatementImpl extends TAbstractMethodStatement {

    private String caller;



    public simTL4J_simTL_TMethodStatementImpl(
        String caller    ) {
        super(
        );
        this.caller = caller;
    }


    public String getCaller() {
        return caller;
    }

    public void setCaller(String caller) {
        this.caller = caller;
    }


}