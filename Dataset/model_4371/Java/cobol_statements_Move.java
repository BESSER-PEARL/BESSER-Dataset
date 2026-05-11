





import java.util.List;
import java.util.ArrayList;

public class cobol_statements_Move extends Statement {

    private String corresponding;



    public cobol_statements_Move(
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