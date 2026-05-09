





import java.util.List;
import java.util.ArrayList;

public class gastm_PrimitiveType extends DataType {

    private boolean isSigned;



    public gastm_PrimitiveType(
        boolean isSigned    ) {
        super(
        );
        this.isSigned = isSigned;
    }


    public boolean getIssigned() {
        return isSigned;
    }

    public void setIssigned(boolean isSigned) {
        this.isSigned = isSigned;
    }


}