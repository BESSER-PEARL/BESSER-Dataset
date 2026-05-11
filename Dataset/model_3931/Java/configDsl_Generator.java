





import java.util.List;
import java.util.ArrayList;

public class configDsl_Generator  {

    private String genClass;
    private String bundle;
    private String name;





    private configDsl_Config configdsl_config;




    private configDsl_Config configdsl_config;


    public configDsl_Generator(
        String genClass,        String bundle,        String name    ) {
        this.genClass = genClass;
        this.bundle = bundle;
        this.name = name;
    }


    public String getGenclass() {
        return genClass;
    }

    public void setGenclass(String genClass) {
        this.genClass = genClass;
    }
    public String getBundle() {
        return bundle;
    }

    public void setBundle(String bundle) {
        this.bundle = bundle;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public configDsl_Config getConfigdsl_config() {
        return configdsl_config;
    }

    public void setConfigdsl_config(configDsl_Config configdsl_config) {
        this.configdsl_config = configdsl_config;
    }
    public configDsl_Config getConfigdsl_config() {
        return configdsl_config;
    }

    public void setConfigdsl_config(configDsl_Config configdsl_config) {
        this.configdsl_config = configdsl_config;
    }

}