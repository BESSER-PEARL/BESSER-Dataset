





import java.util.List;
import java.util.ArrayList;

public class model_CUnparsedStatement extends AbstractCStatement {

    private String code;



    public model_CUnparsedStatement(
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