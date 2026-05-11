





import java.util.List;
import java.util.ArrayList;

public class idl_Preproc_If extends Preproc {

    private boolean negation;



    public idl_Preproc_If(
        boolean negation    ) {
        super(
        );
        this.negation = negation;
    }


    public boolean getNegation() {
        return negation;
    }

    public void setNegation(boolean negation) {
        this.negation = negation;
    }


}