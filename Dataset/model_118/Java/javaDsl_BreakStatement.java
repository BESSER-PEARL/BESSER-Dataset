





import java.util.List;
import java.util.ArrayList;

public class javaDsl_BreakStatement extends Statement {

    private String reference;



    public javaDsl_BreakStatement(
        String reference    ) {
        super(
        );
        this.reference = reference;
    }


    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }


}