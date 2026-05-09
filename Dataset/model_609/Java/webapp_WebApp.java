





import java.util.List;
import java.util.ArrayList;

public class webapp_WebApp  {

    private String framework;
    private String name;



    public webapp_WebApp(
        String framework,        String name    ) {
        this.framework = framework;
        this.name = name;
    }


    public String getFramework() {
        return framework;
    }

    public void setFramework(String framework) {
        this.framework = framework;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}