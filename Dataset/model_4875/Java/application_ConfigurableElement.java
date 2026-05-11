





import java.util.List;
import java.util.ArrayList;

public class application_ConfigurableElement  {

    private String ident;
    private String description;
    private String changeable;
    private String hidden;
    private String name;
    private String configurationImage;





    private application_Configuration application_configuration;


    public application_ConfigurableElement(
        String ident,        String description,        String changeable,        String hidden,        String name,        String configurationImage    ) {
        this.ident = ident;
        this.description = description;
        this.changeable = changeable;
        this.hidden = hidden;
        this.name = name;
        this.configurationImage = configurationImage;
    }


    public String getIdent() {
        return ident;
    }

    public void setIdent(String ident) {
        this.ident = ident;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getChangeable() {
        return changeable;
    }

    public void setChangeable(String changeable) {
        this.changeable = changeable;
    }
    public String getHidden() {
        return hidden;
    }

    public void setHidden(String hidden) {
        this.hidden = hidden;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getConfigurationimage() {
        return configurationImage;
    }

    public void setConfigurationimage(String configurationImage) {
        this.configurationImage = configurationImage;
    }

    public application_Configuration getApplication_configuration() {
        return application_configuration;
    }

    public void setApplication_configuration(application_Configuration application_configuration) {
        this.application_configuration = application_configuration;
    }

}