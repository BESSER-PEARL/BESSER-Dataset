





import java.util.List;
import java.util.ArrayList;

public class application_ConfigurableElement  {

    private String configurationImage;
    private String hidden;
    private String changeable;
    private String description;
    private String ident;
    private String name;





    private application_Configuration application_configuration;


    public application_ConfigurableElement(
        String configurationImage,        String hidden,        String changeable,        String description,        String ident,        String name    ) {
        this.configurationImage = configurationImage;
        this.hidden = hidden;
        this.changeable = changeable;
        this.description = description;
        this.ident = ident;
        this.name = name;
    }


    public String getConfigurationimage() {
        return configurationImage;
    }

    public void setConfigurationimage(String configurationImage) {
        this.configurationImage = configurationImage;
    }
    public String getHidden() {
        return hidden;
    }

    public void setHidden(String hidden) {
        this.hidden = hidden;
    }
    public String getChangeable() {
        return changeable;
    }

    public void setChangeable(String changeable) {
        this.changeable = changeable;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getIdent() {
        return ident;
    }

    public void setIdent(String ident) {
        this.ident = ident;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public application_Configuration getApplication_configuration() {
        return application_configuration;
    }

    public void setApplication_configuration(application_Configuration application_configuration) {
        this.application_configuration = application_configuration;
    }

}