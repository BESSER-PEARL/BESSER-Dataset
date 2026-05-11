





import java.util.List;
import java.util.ArrayList;

public class nuSMV_SignedWordType extends SimpleType {

    private String signedNumber;



    public nuSMV_SignedWordType(
        String signedNumber    ) {
        super(
        );
        this.signedNumber = signedNumber;
    }


    public String getSignednumber() {
        return signedNumber;
    }

    public void setSignednumber(String signedNumber) {
        this.signedNumber = signedNumber;
    }


}