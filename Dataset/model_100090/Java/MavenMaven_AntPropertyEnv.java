





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_AntPropertyEnv extends AntProperty {

    private String environment;



    public MavenMaven_AntPropertyEnv(
        String environment    ) {
        super(
        );
        this.environment = environment;
    }


    public String getEnvironment() {
        return environment;
    }

    public void setEnvironment(String environment) {
        this.environment = environment;
    }


}