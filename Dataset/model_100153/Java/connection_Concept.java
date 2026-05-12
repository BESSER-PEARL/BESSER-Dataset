





import java.util.List;
import java.util.ArrayList;

public class connection_Concept extends TdTable {

    private String LoopLimit;
    private String LoopExpression;





    private connection_MDMConnection connection_mdmconnection;


    public connection_Concept(
        String LoopLimit,        String LoopExpression    ) {
        super(
        );
        this.LoopLimit = LoopLimit;
        this.LoopExpression = LoopExpression;
    }


    public String getLooplimit() {
        return LoopLimit;
    }

    public void setLooplimit(String LoopLimit) {
        this.LoopLimit = LoopLimit;
    }
    public String getLoopexpression() {
        return LoopExpression;
    }

    public void setLoopexpression(String LoopExpression) {
        this.LoopExpression = LoopExpression;
    }

    public connection_MDMConnection getConnection_mdmconnection() {
        return connection_mdmconnection;
    }

    public void setConnection_mdmconnection(connection_MDMConnection connection_mdmconnection) {
        this.connection_mdmconnection = connection_mdmconnection;
    }

}