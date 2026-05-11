





import java.util.List;
import java.util.ArrayList;

public class securityTest_Attack  {

    private String severity;
    private String name;





    private securityTest_Input securitytest_input;




    private securityTest_Test securitytest_test;


    public securityTest_Attack(
        String severity,        String name    ) {
        this.severity = severity;
        this.name = name;
    }


    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public securityTest_Input getSecuritytest_input() {
        return securitytest_input;
    }

    public void setSecuritytest_input(securityTest_Input securitytest_input) {
        this.securitytest_input = securitytest_input;
    }
    public securityTest_Test getSecuritytest_test() {
        return securitytest_test;
    }

    public void setSecuritytest_test(securityTest_Test securitytest_test) {
        this.securitytest_test = securitytest_test;
    }

}