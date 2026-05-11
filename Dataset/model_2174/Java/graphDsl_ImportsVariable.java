





import java.util.List;
import java.util.ArrayList;

public class graphDsl_ImportsVariable  {

    private boolean isExternal;
    private String componentName;
    private String componentProperty;
    private boolean isOptional;





    private graphDsl_ImportsProperty graphdsl_importsproperty;


    public graphDsl_ImportsVariable(
        boolean isExternal,        String componentName,        String componentProperty,        boolean isOptional    ) {
        this.isExternal = isExternal;
        this.componentName = componentName;
        this.componentProperty = componentProperty;
        this.isOptional = isOptional;
    }


    public boolean getIsexternal() {
        return isExternal;
    }

    public void setIsexternal(boolean isExternal) {
        this.isExternal = isExternal;
    }
    public String getComponentname() {
        return componentName;
    }

    public void setComponentname(String componentName) {
        this.componentName = componentName;
    }
    public String getComponentproperty() {
        return componentProperty;
    }

    public void setComponentproperty(String componentProperty) {
        this.componentProperty = componentProperty;
    }
    public boolean getIsoptional() {
        return isOptional;
    }

    public void setIsoptional(boolean isOptional) {
        this.isOptional = isOptional;
    }

    public graphDsl_ImportsProperty getGraphdsl_importsproperty() {
        return graphdsl_importsproperty;
    }

    public void setGraphdsl_importsproperty(graphDsl_ImportsProperty graphdsl_importsproperty) {
        this.graphdsl_importsproperty = graphdsl_importsproperty;
    }

}