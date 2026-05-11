





import java.util.List;
import java.util.ArrayList;

public class NQC_Label  {

    private String Label;





    private NQC_Statement nqc_statement;


    public NQC_Label(
        String Label    ) {
        this.Label = Label;
    }


    public String getLabel() {
        return Label;
    }

    public void setLabel(String Label) {
        this.Label = Label;
    }

    public NQC_Statement getNqc_statement() {
        return nqc_statement;
    }

    public void setNqc_statement(NQC_Statement nqc_statement) {
        this.nqc_statement = nqc_statement;
    }

}