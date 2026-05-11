





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlConstantLiteral extends SadlExplicitValueLiteral {

    private String term;



    public sADL_SadlConstantLiteral(
        String term    ) {
        super(
        );
        this.term = term;
    }


    public String getTerm() {
        return term;
    }

    public void setTerm(String term) {
        this.term = term;
    }


}