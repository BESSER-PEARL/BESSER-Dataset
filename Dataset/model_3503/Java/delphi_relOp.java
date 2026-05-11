





import java.util.List;
import java.util.ArrayList;

public class delphi_relOp extends CSTrace {

    private String op;





    private delphi_relExp delphi_relexp;


    public delphi_relOp(
        String op    ) {
        super(
        );
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public delphi_relExp getDelphi_relexp() {
        return delphi_relexp;
    }

    public void setDelphi_relexp(delphi_relExp delphi_relexp) {
        this.delphi_relexp = delphi_relexp;
    }

}