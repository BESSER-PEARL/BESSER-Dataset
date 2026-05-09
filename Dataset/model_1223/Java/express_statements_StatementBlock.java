





import java.util.List;
import java.util.ArrayList;

public class express_statements_StatementBlock extends Statement {

    private String delimited;



    public express_statements_StatementBlock(
        String delimited    ) {
        super(
        );
        this.delimited = delimited;
    }


    public String getDelimited() {
        return delimited;
    }

    public void setDelimited(String delimited) {
        this.delimited = delimited;
    }


}