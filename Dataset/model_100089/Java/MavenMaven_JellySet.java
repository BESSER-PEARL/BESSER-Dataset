





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_JellySet extends JellyCommand {

    private String var;
    private String value;



    public MavenMaven_JellySet(
        String var,        String value    ) {
        super(
        );
        this.var = var;
        this.value = value;
    }


    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}