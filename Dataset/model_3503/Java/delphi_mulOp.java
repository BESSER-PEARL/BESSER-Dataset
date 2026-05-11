





import java.util.List;
import java.util.ArrayList;

public class delphi_mulOp extends CSTrace {

    private String op;





    private delphi_multExp delphi_multexp;


    public delphi_mulOp(
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

    public delphi_multExp getDelphi_multexp() {
        return delphi_multexp;
    }

    public void setDelphi_multexp(delphi_multExp delphi_multexp) {
        this.delphi_multexp = delphi_multexp;
    }

}