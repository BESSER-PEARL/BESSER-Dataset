





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_JellySet extends JellyCommand {

    private String value;
    private String var;



    public MavenMaven_JellySet(
        String value,        String var    ) {
        super(
        );
        this.value = value;
        this.var = var;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }


}