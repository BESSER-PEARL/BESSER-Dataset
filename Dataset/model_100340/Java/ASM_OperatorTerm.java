





import java.util.List;
import java.util.ArrayList;

public class ASM_OperatorTerm extends Term {

    private String opName;



    public ASM_OperatorTerm(
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