





import java.util.List;
import java.util.ArrayList;

public class SecCon_ContextInformation  {

    private String type;
    private String name;





    private SecCon_ContextScenario seccon_contextscenario;


    public SecCon_ContextInformation(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SecCon_ContextScenario getSeccon_contextscenario() {
        return seccon_contextscenario;
    }

    public void setSeccon_contextscenario(SecCon_ContextScenario seccon_contextscenario) {
        this.seccon_contextscenario = seccon_contextscenario;
    }

}