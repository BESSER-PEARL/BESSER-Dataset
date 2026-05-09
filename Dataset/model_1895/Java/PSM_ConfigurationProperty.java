





import java.util.List;
import java.util.ArrayList;

public class PSM_ConfigurationProperty extends ArtifactElement {

    private String PropertyValue;
    private String ConfigurationProfile;
    private String FullyQualifiedPropertyName;





    private PSM_JavaSpringWebApplicationProject psm_javaspringwebapplicationproject;


    public PSM_ConfigurationProperty(
        String PropertyValue,        String ConfigurationProfile,        String FullyQualifiedPropertyName    ) {
        super(
        );
        this.PropertyValue = PropertyValue;
        this.ConfigurationProfile = ConfigurationProfile;
        this.FullyQualifiedPropertyName = FullyQualifiedPropertyName;
    }


    public String getPropertyvalue() {
        return PropertyValue;
    }

    public void setPropertyvalue(String PropertyValue) {
        this.PropertyValue = PropertyValue;
    }
    public String getConfigurationprofile() {
        return ConfigurationProfile;
    }

    public void setConfigurationprofile(String ConfigurationProfile) {
        this.ConfigurationProfile = ConfigurationProfile;
    }
    public String getFullyqualifiedpropertyname() {
        return FullyQualifiedPropertyName;
    }

    public void setFullyqualifiedpropertyname(String FullyQualifiedPropertyName) {
        this.FullyQualifiedPropertyName = FullyQualifiedPropertyName;
    }

    public PSM_JavaSpringWebApplicationProject getPsm_javaspringwebapplicationproject() {
        return psm_javaspringwebapplicationproject;
    }

    public void setPsm_javaspringwebapplicationproject(PSM_JavaSpringWebApplicationProject psm_javaspringwebapplicationproject) {
        this.psm_javaspringwebapplicationproject = psm_javaspringwebapplicationproject;
    }

}