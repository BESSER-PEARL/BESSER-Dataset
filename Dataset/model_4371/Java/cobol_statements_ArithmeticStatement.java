





import java.util.List;
import java.util.ArrayList;

public class cobol_statements_ArithmeticStatement extends statements_Statement, statements_ErrorHandled {

    private String corresponding;



    public cobol_statements_ArithmeticStatement(
        String corresponding    ) {
        super(
        );
        this.corresponding = corresponding;
    }


    public String getCorresponding() {
        return corresponding;
    }

    public void setCorresponding(String corresponding) {
        this.corresponding = corresponding;
    }


}