





import java.util.List;
import java.util.ArrayList;

public class behaviour_Variable extends Expression {

    private String varName;



    public behaviour_Variable(
        String varName    ) {
        super(
        );
        this.varName = varName;
    }


    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }


}