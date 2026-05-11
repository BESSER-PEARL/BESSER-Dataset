





import java.util.List;
import java.util.ArrayList;

public class aDSL_SharedDef extends VarDef, Member, Statement {

    private boolean replicas;
    private String name;





    private aDSL_VariableType adsl_variabletype;


    public aDSL_SharedDef(
        boolean replicas,        String name    ) {
        super(
        );
        this.replicas = replicas;
        this.name = name;
    }


    public boolean getReplicas() {
        return replicas;
    }

    public void setReplicas(boolean replicas) {
        this.replicas = replicas;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public aDSL_VariableType getAdsl_variabletype() {
        return adsl_variabletype;
    }

    public void setAdsl_variabletype(aDSL_VariableType adsl_variabletype) {
        this.adsl_variabletype = adsl_variabletype;
    }

}