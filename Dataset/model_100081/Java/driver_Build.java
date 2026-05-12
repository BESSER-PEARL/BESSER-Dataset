





import java.util.List;
import java.util.ArrayList;

public class driver_Build  {

    private String componentName;
    private String testBuild;
    private String uRI;



    public driver_Build(
        String componentName,        String testBuild,        String uRI    ) {
        this.componentName = componentName;
        this.testBuild = testBuild;
        this.uRI = uRI;
    }


    public String getComponentname() {
        return componentName;
    }

    public void setComponentname(String componentName) {
        this.componentName = componentName;
    }
    public String getTestbuild() {
        return testBuild;
    }

    public void setTestbuild(String testBuild) {
        this.testBuild = testBuild;
    }
    public String getUri() {
        return uRI;
    }

    public void setUri(String uRI) {
        this.uRI = uRI;
    }


}