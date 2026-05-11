





import java.util.List;
import java.util.ArrayList;

public class dsl_GooglecontactPUT extends Action {

    private String value;
    private String dbSrc;
    private String impersonatedUser;
    private String project;
    private String ptwelveFile;
    private String account;
    private String privateKey;



    public dsl_GooglecontactPUT(
        String value,        String dbSrc,        String impersonatedUser,        String project,        String ptwelveFile,        String account,        String privateKey    ) {
        super(
        );
        this.value = value;
        this.dbSrc = dbSrc;
        this.impersonatedUser = impersonatedUser;
        this.project = project;
        this.ptwelveFile = ptwelveFile;
        this.account = account;
        this.privateKey = privateKey;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getDbsrc() {
        return dbSrc;
    }

    public void setDbsrc(String dbSrc) {
        this.dbSrc = dbSrc;
    }
    public String getImpersonateduser() {
        return impersonatedUser;
    }

    public void setImpersonateduser(String impersonatedUser) {
        this.impersonatedUser = impersonatedUser;
    }
    public String getProject() {
        return project;
    }

    public void setProject(String project) {
        this.project = project;
    }
    public String getPtwelvefile() {
        return ptwelveFile;
    }

    public void setPtwelvefile(String ptwelveFile) {
        this.ptwelveFile = ptwelveFile;
    }
    public String getAccount() {
        return account;
    }

    public void setAccount(String account) {
        this.account = account;
    }
    public String getPrivatekey() {
        return privateKey;
    }

    public void setPrivatekey(String privateKey) {
        this.privateKey = privateKey;
    }


}