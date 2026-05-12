





import java.util.List;
import java.util.ArrayList;

public class Error_code  {

    private String Code_Id;
    private String Code_Exp;
    private String Code_serial;



    public Error_code(
        String Code_Id,        String Code_Exp,        String Code_serial    ) {
        this.Code_Id = Code_Id;
        this.Code_Exp = Code_Exp;
        this.Code_serial = Code_serial;
    }


    public String getCode_id() {
        return Code_Id;
    }

    public void setCode_id(String Code_Id) {
        this.Code_Id = Code_Id;
    }
    public String getCode_exp() {
        return Code_Exp;
    }

    public void setCode_exp(String Code_Exp) {
        this.Code_Exp = Code_Exp;
    }
    public String getCode_serial() {
        return Code_serial;
    }

    public void setCode_serial(String Code_serial) {
        this.Code_serial = Code_serial;
    }


}