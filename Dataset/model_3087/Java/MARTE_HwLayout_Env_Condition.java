





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwLayout_Env_Condition  {

    private String type;
    private String status;





    private NFP_String nfp_string;




    private Realnterval realnterval;


    public MARTE_HwLayout_Env_Condition(
        String type,        String status    ) {
        this.type = type;
        this.status = status;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public NFP_String getNfp_string() {
        return nfp_string;
    }

    public void setNfp_string(NFP_String nfp_string) {
        this.nfp_string = nfp_string;
    }
    public Realnterval getRealnterval() {
        return realnterval;
    }

    public void setRealnterval(Realnterval realnterval) {
        this.realnterval = realnterval;
    }

}