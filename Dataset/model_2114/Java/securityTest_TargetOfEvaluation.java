





import java.util.List;
import java.util.ArrayList;

public class securityTest_TargetOfEvaluation  {

    private String protocol;
    private String domain;
    private String port;
    private String ip;





    private securityTest_Test securitytest_test;


    public securityTest_TargetOfEvaluation(
        String protocol,        String domain,        String port,        String ip    ) {
        this.protocol = protocol;
        this.domain = domain;
        this.port = port;
        this.ip = ip;
    }


    public String getProtocol() {
        return protocol;
    }

    public void setProtocol(String protocol) {
        this.protocol = protocol;
    }
    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }
    public String getPort() {
        return port;
    }

    public void setPort(String port) {
        this.port = port;
    }
    public String getIp() {
        return ip;
    }

    public void setIp(String ip) {
        this.ip = ip;
    }

    public securityTest_Test getSecuritytest_test() {
        return securitytest_test;
    }

    public void setSecuritytest_test(securityTest_Test securitytest_test) {
        this.securitytest_test = securitytest_test;
    }

}