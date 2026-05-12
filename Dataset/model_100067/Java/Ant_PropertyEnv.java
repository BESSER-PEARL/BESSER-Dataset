





import java.util.List;
import java.util.ArrayList;

public class Ant_PropertyEnv extends Property {

    private String environment;



    public Ant_PropertyEnv(
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