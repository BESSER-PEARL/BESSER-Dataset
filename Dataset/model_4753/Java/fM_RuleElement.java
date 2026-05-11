





import java.util.List;
import java.util.ArrayList;

public class fM_RuleElement extends Formula {

    private String close_operator;
    private String open_operator;



    public fM_RuleElement(
        String close_operator,        String open_operator    ) {
        super(
        );
        this.close_operator = close_operator;
        this.open_operator = open_operator;
    }


    public String getClose_operator() {
        return close_operator;
    }

    public void setClose_operator(String close_operator) {
        this.close_operator = close_operator;
    }
    public String getOpen_operator() {
        return open_operator;
    }

    public void setOpen_operator(String open_operator) {
        this.open_operator = open_operator;
    }


}