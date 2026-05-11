





import java.util.List;
import java.util.ArrayList;

public class model_xbase_XFeatureCall extends XAbstractFeatureCall {

    private boolean typeLiteral;
    private boolean packageFragment;
    private boolean explicitOperationCall;
    private boolean indexedOperation;





    private List<XExpression> xexpressions;




    private XExpression xexpression;


    public model_xbase_XFeatureCall(
        boolean typeLiteral,        boolean packageFragment,        boolean explicitOperationCall,        boolean indexedOperation    ) {
        super(
        );
        this.typeLiteral = typeLiteral;
        this.packageFragment = packageFragment;
        this.explicitOperationCall = explicitOperationCall;
        this.indexedOperation = indexedOperation;
        this.xexpressions = new ArrayList<>();
    }

    public model_xbase_XFeatureCall(
        boolean typeLiteral,        boolean packageFragment,        boolean explicitOperationCall,        boolean indexedOperation        ArrayList<XExpression> xexpressions    ) {
        this.typeLiteral = typeLiteral;
        this.packageFragment = packageFragment;
        this.explicitOperationCall = explicitOperationCall;
        this.indexedOperation = indexedOperation;
        this.xexpressions = xexpressions;
    }

    public boolean getTypeliteral() {
        return typeLiteral;
    }

    public void setTypeliteral(boolean typeLiteral) {
        this.typeLiteral = typeLiteral;
    }
    public boolean getPackagefragment() {
        return packageFragment;
    }

    public void setPackagefragment(boolean packageFragment) {
        this.packageFragment = packageFragment;
    }
    public boolean getExplicitoperationcall() {
        return explicitOperationCall;
    }

    public void setExplicitoperationcall(boolean explicitOperationCall) {
        this.explicitOperationCall = explicitOperationCall;
    }
    public boolean getIndexedoperation() {
        return indexedOperation;
    }

    public void setIndexedoperation(boolean indexedOperation) {
        this.indexedOperation = indexedOperation;
    }

    public List<XExpression> getXexpressions() {
        return xexpressions;
    }

    public void addXexpression(Xexpression xexpression) {
        this.xexpressions.add(xexpression);
    }
    public XExpression getXexpression() {
        return xexpression;
    }

    public void setXexpression(XExpression xexpression) {
        this.xexpression = xexpression;
    }

}