





import java.util.List;
import java.util.ArrayList;

public class xtend_XFeatureCall extends XAbstractFeatureCall {

    private boolean explicitOperationCall;



    public xtend_XFeatureCall(
        boolean explicitOperationCall    ) {
        super(
        );
        this.explicitOperationCall = explicitOperationCall;
    }


    public boolean getExplicitoperationcall() {
        return explicitOperationCall;
    }

    public void setExplicitoperationcall(boolean explicitOperationCall) {
        this.explicitOperationCall = explicitOperationCall;
    }


}