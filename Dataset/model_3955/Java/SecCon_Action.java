





import java.util.List;
import java.util.ArrayList;

public class SecCon_Action  {

    private String parameter;
    private String name;





    private SecCon_Rule seccon_rule;


    public SecCon_Action(
        String parameter,        String name    ) {
        this.parameter = parameter;
        this.name = name;
    }


    public String getParameter() {
        return parameter;
    }

    public void setParameter(String parameter) {
        this.parameter = parameter;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SecCon_Rule getSeccon_rule() {
        return seccon_rule;
    }

    public void setSeccon_rule(SecCon_Rule seccon_rule) {
        this.seccon_rule = seccon_rule;
    }

}