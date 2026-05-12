





import java.util.List;
import java.util.ArrayList;

public class connection_Concept extends TdTable {

    private String LoopExpression;
    private String conceptType;
    private String xPathPrefix;
    private boolean inputModel;
    private String LoopLimit;





    private connection_MDMConnection connection_mdmconnection;


    public connection_Concept(
        String LoopExpression,        String conceptType,        String xPathPrefix,        boolean inputModel,        String LoopLimit    ) {
        super(
        );
        this.LoopExpression = LoopExpression;
        this.conceptType = conceptType;
        this.xPathPrefix = xPathPrefix;
        this.inputModel = inputModel;
        this.LoopLimit = LoopLimit;
    }


    public String getLoopexpression() {
        return LoopExpression;
    }

    public void setLoopexpression(String LoopExpression) {
        this.LoopExpression = LoopExpression;
    }
    public String getConcepttype() {
        return conceptType;
    }

    public void setConcepttype(String conceptType) {
        this.conceptType = conceptType;
    }
    public String getXpathprefix() {
        return xPathPrefix;
    }

    public void setXpathprefix(String xPathPrefix) {
        this.xPathPrefix = xPathPrefix;
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