





import java.util.List;
import java.util.ArrayList;

public class connection_Concept extends TdTable {

    private boolean inputModel;
    private String LoopExpression;
    private String LoopLimit;





    private connection_MDMConnection connection_mdmconnection;


    public connection_Concept(
        boolean inputModel,        String LoopExpression,        String LoopLimit    ) {
        super(
        );
        this.inputModel = inputModel;
        this.LoopExpression = LoopExpression;
        this.LoopLimit = LoopLimit;
    }


    public boolean getInputmodel() {
        return inputModel;
    }

    public void setInputmodel(boolean inputModel) {
        this.inputModel = inputModel;
    }
    public String getLoopexpression() {
        return LoopExpression;
    }

    public void setLoopexpression(String LoopExpression) {
        this.LoopExpression = LoopExpression;
    }
    public String getLooplimit() {
        return LoopLimit;
    }

    public void setLooplimit(String LoopLimit) {
        this.LoopLimit = LoopLimit;
    }

    public connection_MDMConnection getConnection_mdmconnection() {
        return connection_mdmconnection;
    }

    public void setConnection_mdmconnection(connection_MDMConnection connection_mdmconnection) {
        this.connection_mdmconnection = connection_mdmconnection;
    }

}