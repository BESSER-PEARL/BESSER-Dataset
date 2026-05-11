





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDAnnotation extends xsd_XSDComponent, xsd_XSDRedefineContent {

    private String userInformation;
    private String applicationInformation;
    private String attributes;



    public model_xsd_XSDAnnotation(
        String userInformation,        String applicationInformation,        String attributes    ) {
        super(
        );
        this.userInformation = userInformation;
        this.applicationInformation = applicationInformation;
        this.attributes = attributes;
    }


    public String getUserinformation() {
        return userInformation;
    }

    public void setUserinformation(String userInformation) {
        this.userInformation = userInformation;
    }
    public String getApplicationinformation() {
        return applicationInformation;
    }

    public void setApplicationinformation(String applicationInformation) {
        this.applicationInformation = applicationInformation;
    }
    public String getAttributes() {
        return attributes;
    }

    public void setAttributes(String attributes) {
        this.attributes = attributes;
    }


}