





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_UnaryExp extends Exp {

    private String op;





    private deviceModelingLanguage_Exp devicemodelinglanguage_exp;


    public deviceModelingLanguage_UnaryExp(
        String op    ) {
        super(
        );
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public deviceModelingLanguage_Exp getDevicemodelinglanguage_exp() {
        return devicemodelinglanguage_exp;
    }

    public void setDevicemodelinglanguage_exp(deviceModelingLanguage_Exp devicemodelinglanguage_exp) {
        this.devicemodelinglanguage_exp = devicemodelinglanguage_exp;
    }

}