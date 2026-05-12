





import java.util.List;
import java.util.ArrayList;

public class History  {

    private String Code_id;
    private String Code_amount;



    public History(
        String Code_id,        String Code_amount    ) {
        this.Code_id = Code_id;
        this.Code_amount = Code_amount;
    }


    public String getCode_id() {
        return Code_id;
    }

    public void setCode_id(String Code_id) {
        this.Code_id = Code_id;
    }
    public String getCode_amount() {
        return Code_amount;
    }

    public void setCode_amount(String Code_amount) {
        this.Code_amount = Code_amount;
    }


}