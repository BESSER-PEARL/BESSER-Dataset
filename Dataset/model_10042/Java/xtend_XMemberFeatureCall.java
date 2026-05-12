





import java.util.List;
import java.util.ArrayList;

public class xtend_XMemberFeatureCall extends XAbstractFeatureCall {

    private boolean nullSafe;
    private boolean spreading;
    private boolean explicitOperationCall;



    public xtend_XMemberFeatureCall(
        boolean nullSafe,        boolean spreading,        boolean explicitOperationCall    ) {
        super(
        );
        this.nullSafe = nullSafe;
        this.spreading = spreading;
        this.explicitOperationCall = explicitOperationCall;
    }


    public boolean getNullsafe() {
        return nullSafe;
    }

    public void setNullsafe(boolean nullSafe) {
        this.nullSafe = nullSafe;
    }
    public boolean getSpreading() {
        return spreading;
    }

    public void setSpreading(boolean spreading) {
        this.spreading = spreading;
    }
    public boolean getExplicitoperationcall() {
        return explicitOperationCall;
    }

    public void setExplicitoperationcall(boolean explicitOperationCall) {
        this.explicitOperationCall = explicitOperationCall;
    }


}