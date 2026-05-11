





import java.util.List;
import java.util.ArrayList;

public class cobol_statements_SetIndexName extends SetStatement {

    private String adjust;



    public cobol_statements_SetIndexName(
        String adjust    ) {
        super(
        );
        this.adjust = adjust;
    }


    public String getAdjust() {
        return adjust;
    }

    public void setAdjust(String adjust) {
        this.adjust = adjust;
    }


}