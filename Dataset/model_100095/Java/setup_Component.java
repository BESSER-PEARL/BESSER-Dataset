





import java.util.List;
import java.util.ArrayList;

public class setup_Component  {

    private String name;
    private String versionRange;
    private String type;





    private setup_MaterializationTask setup_materializationtask;


    public setup_Component(
        String name,        String versionRange,        String type    ) {
        this.name = name;
        this.versionRange = versionRange;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVersionrange() {
        return versionRange;
    }

    public void setVersionrange(String versionRange) {
        this.versionRange = versionRange;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public setup_MaterializationTask getSetup_materializationtask() {
        return setup_materializationtask;
    }

    public void setSetup_materializationtask(setup_MaterializationTask setup_materializationtask) {
        this.setup_materializationtask = setup_materializationtask;
    }

}