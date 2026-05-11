





import java.util.List;
import java.util.ArrayList;

public class securityTest_AuthSetting  {

    private String logoutMessagePattern;
    private String passwordParam;
    private String loginTargetURL;
    private String usernameParam;
    private String loginMessagePattern;
    private String roles;





    private securityTest_Test securitytest_test;


    public securityTest_AuthSetting(
        String logoutMessagePattern,        String passwordParam,        String loginTargetURL,        String usernameParam,        String loginMessagePattern,        String roles    ) {
        this.logoutMessagePattern = logoutMessagePattern;
        this.passwordParam = passwordParam;
        this.loginTargetURL = loginTargetURL;
        this.usernameParam = usernameParam;
        this.loginMessagePattern = loginMessagePattern;
        this.roles = roles;
    }


    public String getLogoutmessagepattern() {
        return logoutMessagePattern;
    }

    public void setLogoutmessagepattern(String logoutMessagePattern) {
        this.logoutMessagePattern = logoutMessagePattern;
    }
    public String getPasswordparam() {
        return passwordParam;
    }

    public void setPasswordparam(String passwordParam) {
        this.passwordParam = passwordParam;
    }
    public String getLogintargeturl() {
        return loginTargetURL;
    }

    public void setLogintargeturl(String loginTargetURL) {
        this.loginTargetURL = loginTargetURL;
    }
    public String getUsernameparam() {
        return usernameParam;
    }

    public void setUsernameparam(String usernameParam) {
        this.usernameParam = usernameParam;
    }
    public String getLoginmessagepattern() {
        return loginMessagePattern;
    }

    public void setLoginmessagepattern(String loginMessagePattern) {
        this.loginMessagePattern = loginMessagePattern;
    }
    public String getRoles() {
        return roles;
    }

    public void setRoles(String roles) {
        this.roles = roles;
    }

    public securityTest_Test getSecuritytest_test() {
        return securitytest_test;
    }

    public void setSecuritytest_test(securityTest_Test securitytest_test) {
        this.securitytest_test = securitytest_test;
    }

}