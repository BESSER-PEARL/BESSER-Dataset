





import java.util.List;
import java.util.ArrayList;

public class nuSMV_UnsignedWordType extends SimpleType {

    private String uWordNumber;



    public nuSMV_UnsignedWordType(
        String uWordNumber    ) {
        super(
        );
        this.uWordNumber = uWordNumber;
    }


    public String getUwordnumber() {
        return uWordNumber;
    }

    public void setUwordnumber(String uWordNumber) {
        this.uWordNumber = uWordNumber;
    }


}