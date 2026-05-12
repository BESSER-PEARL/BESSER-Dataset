





import java.util.List;
import java.util.ArrayList;

public class connection_Concept extends TdTable {

    private String LoopExpression;
    private boolean inputModel;
    private String LoopLimit;





    private connection_MDMConnection connection_mdmconnection;


    public connection_Concept(
        String LoopExpression,        boolean inputModel,        String LoopLimit    ) {
        super(
        );
        this.LoopExpression = LoopExpression;
        this.inputModel = inputModel;
        this.LoopLimit = LoopLimit;
    }


    public String getLoopexpression() {
        return LoopExpression;
    }

    public void setLoopexpression(String LoopExpression) {
        this.LoopExpression = LoopExpression;
    }
    public boolean getInputmodel() {
        return inputModel;
    }

    public void setInputmodel(boolean inputModel) {
        this.inputModel = inputModel;
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