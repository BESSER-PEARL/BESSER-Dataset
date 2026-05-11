





import java.util.List;
import java.util.ArrayList;

public class jsm_CUnparsedStatement extends AbstractCStatement {

    private String code;



    public jsm_CUnparsedStatement(
        String code    ) {
        super(
        );
        this.code = code;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }


}