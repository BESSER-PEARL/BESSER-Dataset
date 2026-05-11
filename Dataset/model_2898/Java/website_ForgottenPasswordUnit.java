





import java.util.List;
import java.util.ArrayList;

public class website_ForgottenPasswordUnit extends ControlUnit, AuthenticationUnit {

    private String styleClass;





    private website_LocalAuthenticationSystem website_localauthenticationsystem;


    public website_ForgottenPasswordUnit(
        String styleClass    ) {
        super(
        );
        this.styleClass = styleClass;
    }


    public String getStyleclass() {
        return styleClass;
    }

    public void setStyleclass(String styleClass) {
        this.styleClass = styleClass;
    }

    public website_LocalAuthenticationSystem getWebsite_localauthenticationsystem() {
        return website_localauthenticationsystem;
    }

    public void setWebsite_localauthenticationsystem(website_LocalAuthenticationSystem website_localauthenticationsystem) {
        this.website_localauthenticationsystem = website_localauthenticationsystem;
    }

}