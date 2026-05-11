





import java.util.List;
import java.util.ArrayList;

public class website_LoginUnit extends ControlUnit, AuthenticationUnit {

    private String styleClass;
    private String logoutUriElement;





    private website_LocalAuthenticationSystem website_localauthenticationsystem;


    public website_LoginUnit(
        String styleClass,        String logoutUriElement    ) {
        super(
        );
        this.styleClass = styleClass;
        this.logoutUriElement = logoutUriElement;
    }


    public String getStyleclass() {
        return styleClass;
    }

    public void setStyleclass(String styleClass) {
        this.styleClass = styleClass;
    }
    public String getLogouturielement() {
        return logoutUriElement;
    }

    public void setLogouturielement(String logoutUriElement) {
        this.logoutUriElement = logoutUriElement;
    }

    public website_LocalAuthenticationSystem getWebsite_localauthenticationsystem() {
        return website_localauthenticationsystem;
    }

    public void setWebsite_localauthenticationsystem(website_LocalAuthenticationSystem website_localauthenticationsystem) {
        this.website_localauthenticationsystem = website_localauthenticationsystem;
    }

}