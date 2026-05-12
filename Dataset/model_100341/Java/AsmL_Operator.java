





import java.util.List;
import java.util.ArrayList;

public class AsmL_Operator extends Term {

    private String opName;



    public AsmL_Operator(
        String opName    ) {
        super(
        );
        this.opName = opName;
    }


    public String getOpname() {
        return opName;
    }

    public void setOpname(String opName) {
        this.opName = opName;
    }


}