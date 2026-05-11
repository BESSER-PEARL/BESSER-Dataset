





import java.util.List;
import java.util.ArrayList;

public class uitf_AssertInState extends Statement {

    private String stateId;



    public uitf_AssertInState(
        String stateId    ) {
        super(
        );
        this.stateId = stateId;
    }


    public String getStateid() {
        return stateId;
    }

    public void setStateid(String stateId) {
        this.stateId = stateId;
    }


}