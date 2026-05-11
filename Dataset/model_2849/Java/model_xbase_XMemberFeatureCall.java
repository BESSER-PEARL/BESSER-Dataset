





import java.util.List;
import java.util.ArrayList;

public class model_xbase_XMemberFeatureCall extends XAbstractFeatureCall {

    private boolean packageFragment;
    private boolean typeLiteral;
    private boolean indexedOperation;
    private boolean staticWithDeclaringType;
    private boolean explicitStatic;
    private boolean explicitOperationCall;
    private boolean nullSafe;





    private XExpression xexpression;




    private List<XExpression> xexpressions;


    public model_xbase_XMemberFeatureCall(
        boolean packageFragment,        boolean typeLiteral,        boolean indexedOperation,        boolean staticWithDeclaringType,        boolean explicitStatic,        boolean explicitOperationCall,        boolean nullSafe    ) {
        super(
        );
        this.packageFragment = packageFragment;
        this.typeLiteral = typeLiteral;
        this.indexedOperation = indexedOperation;
        this.staticWithDeclaringType = staticWithDeclaringType;
        this.explicitStatic = explicitStatic;
        this.explicitOperationCall = explicitOperationCall;
        this.nullSafe = nullSafe;
        this.xexpressions = new ArrayList<>();
    }

    public model_xbase_XMemberFeatureCall(
        boolean packageFragment,        boolean typeLiteral,        boolean indexedOperation,        boolean staticWithDeclaringType,        boolean explicitStatic,        boolean explicitOperationCall,        boolean nullSafe        ArrayList<XExpression> xexpressions    ) {
        this.packageFragment = packageFragment;
        this.typeLiteral = typeLiteral;
        this.indexedOperation = indexedOperation;
        this.staticWithDeclaringType = staticWithDeclaringType;
        this.explicitStatic = explicitStatic;
        this.explicitOperationCall = explicitOperationCall;
        this.nullSafe = nullSafe;
        this.xexpressions = xexpressions;
    }

    public boolean getPackagefragment() {
        return packageFragment;
    }

    public void setPackagefragment(boolean packageFragment) {
        this.packageFragment = packageFragment;
    }
    public boolean getTypeliteral() {
        return typeLiteral;
    }

    public void setTypeliteral(boolean typeLiteral) {
        this.typeLiteral = typeLiteral;
    }
    public boolean getIndexedoperation() {
        return indexedOperation;
    }

    public void setIndexedoperation(boolean indexedOperation) {
        this.indexedOperation = indexedOperation;
    }
    public boolean getStaticwithdeclaringtype() {
        return staticWithDeclaringType;
    }

    public void setStaticwithdeclaringtype(boolean staticWithDeclaringType) {
        this.staticWithDeclaringType = staticWithDeclaringType;
    }
    public boolean getExplicitstatic() {
        return explicitStatic;
    }

    public void setExplicitstatic(boolean explicitStatic) {
        this.explicitStatic = explicitStatic;
    }
    public boolean getExplicitoperationcall() {
        return explicitOperationCall;
    }

    public void setExplicitoperationcall(boolean explicitOperationCall) {
        this.explicitOperationCall = explicitOperationCall;
    }
    public boolean getNullsafe() {
        return nullSafe;
    }

    public void setNullsafe(boolean nullSafe) {
        this.nullSafe = nullSafe;
    }

    public XExpression getXexpression() {
        return xexpression;
    }

    public void setXexpression(XExpression xexpression) {
        this.xexpression = xexpression;
    }
    public List<XExpression> getXexpressions() {
        return xexpressions;
    }

    public void addXexpression(Xexpression xexpression) {
        this.xexpressions.add(xexpression);
    }

}