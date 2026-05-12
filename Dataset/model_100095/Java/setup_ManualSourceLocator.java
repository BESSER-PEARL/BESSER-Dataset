





import java.util.List;
import java.util.ArrayList;

public class setup_ManualSourceLocator extends SourceLocator {

    private String componentTypes;
    private String componentNamePattern;
    private String location;



    public setup_ManualSourceLocator(
        String componentTypes,        String componentNamePattern,        String location    ) {
        super(
        );
        this.componentTypes = componentTypes;
        this.componentNamePattern = componentNamePattern;
        this.location = location;
    }


    public String getComponenttypes() {
        return componentTypes;
    }

    public void setComponenttypes(String componentTypes) {
        this.componentTypes = componentTypes;
    }
    public String getComponentnamepattern() {
        return componentNamePattern;
    }

    public void setComponentnamepattern(String componentNamePattern) {
        this.componentNamePattern = componentNamePattern;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}