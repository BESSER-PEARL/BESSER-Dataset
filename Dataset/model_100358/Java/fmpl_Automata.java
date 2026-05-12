





import java.util.List;
import java.util.ArrayList;

public class fmpl_Automata  {

    private String name;





    private fmpl_Policy fmpl_policy;


    public fmpl_Automata(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fmpl_Policy getFmpl_policy() {
        return fmpl_policy;
    }

    public void setFmpl_policy(fmpl_Policy fmpl_policy) {
        this.fmpl_policy = fmpl_policy;
    }

}