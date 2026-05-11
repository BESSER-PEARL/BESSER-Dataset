





import java.util.List;
import java.util.ArrayList;

public class optGrammar_MathematicalFunction extends Literal {

    private String function;



    public optGrammar_MathematicalFunction(
        String function    ) {
        super(
        );
        this.function = function;
    }


    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }


}