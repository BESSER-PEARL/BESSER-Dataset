





import java.util.List;
import java.util.ArrayList;

public class connection_Concept extends TdTable {

    private String xPathPrefix;
    private String conceptType;
    private String LoopLimit;
    private boolean inputModel;
    private String LoopExpression;





    private connection_MDMConnection connection_mdmconnection;


    public connection_Concept(
        String xPathPrefix,        String conceptType,        String LoopLimit,        boolean inputModel,        String LoopExpression    ) {
        super(
        );
        this.xPathPrefix = xPathPrefix;
        this.conceptType = conceptType;
        this.LoopLimit = LoopLimit;
        this.inputModel = inputModel;
        this.LoopExpression = LoopExpression;
    }


    public String getXpathprefix() {
        return xPathPrefix;
    }

    public void setXpathprefix(String xPathPrefix) {
        this.xPathPrefix = xPathPrefix;
    }
    public String getConcepttype() {
        return conceptType;
    }

    public void setConcepttype(String conceptType) {
        this.conceptType = conceptType;
    }
    public String getLooplimit() {
        return LoopLimit;
    }

    public void setLooplimit(String LoopLimit) {
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

    public connection_MDMConnection getConnection_mdmconnection() {
        return connection_mdmconnection;
    }

    public void setConnection_mdmconnection(connection_MDMConnection connection_mdmconnection) {
        this.connection_mdmconnection = connection_mdmconnection;
    }

}