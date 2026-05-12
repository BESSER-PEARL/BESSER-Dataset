





import java.util.List;
import java.util.ArrayList;

public class fsm_VarDecl extends Statement {

    private String key;



    public fsm_VarDecl(
        String key    ) {
        super(
        );
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }


}