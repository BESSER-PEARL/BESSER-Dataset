





import java.util.List;
import java.util.ArrayList;

public class fsm_VarReference extends Expression {

    private String key;



    public fsm_VarReference(
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