





import java.util.List;
import java.util.ArrayList;

public class umlTransition_ChangeEventRule extends EventRule {

    private String exp;



    public umlTransition_ChangeEventRule(
        String exp    ) {
        super(
        );
        this.exp = exp;
    }


    public String getExp() {
        return exp;
    }

    public void setExp(String exp) {
        this.exp = exp;
    }


}