





import java.util.List;
import java.util.ArrayList;

public class gastm_NumberType extends PrimitiveType {

    private String isSigned;



    public gastm_NumberType(
        String isSigned    ) {
        super(
        );
        this.isSigned = isSigned;
    }


    public String getIssigned() {
        return isSigned;
    }

    public void setIssigned(String isSigned) {
        this.isSigned = isSigned;
    }


}