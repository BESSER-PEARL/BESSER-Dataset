





import java.util.List;
import java.util.ArrayList;

public class camel_organisation_CloudCredentials extends Credentials {

    private String publicSSHKey;
    private String username;
    private String name;
    private String securityGroup;
    private String privateSSHKey;
    private String password;



    public camel_organisation_CloudCredentials(
        String publicSSHKey,        String username,        String name,        String securityGroup,        String privateSSHKey,        String password    ) {
        super(
        );
        this.publicSSHKey = publicSSHKey;
        this.username = username;
        this.name = name;
        this.securityGroup = securityGroup;
        this.privateSSHKey = privateSSHKey;
        this.password = password;
    }


    public String getPublicsshkey() {
        return publicSSHKey;
    }

    public void setPublicsshkey(String publicSSHKey) {
        this.publicSSHKey = publicSSHKey;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSecuritygroup() {
        return securityGroup;
    }

    public void setSecuritygroup(String securityGroup) {
        this.securityGroup = securityGroup;
    }
    public String getPrivatesshkey() {
        return privateSSHKey;
    }

    public void setPrivatesshkey(String privateSSHKey) {
        this.privateSSHKey = privateSSHKey;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}