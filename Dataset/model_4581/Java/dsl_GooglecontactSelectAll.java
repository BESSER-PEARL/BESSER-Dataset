





import java.util.List;
import java.util.ArrayList;

public class dsl_GooglecontactSelectAll extends Action {

    private String value;
    private String project;
    private String account;
    private String dbSrc;
    private String ptwelveFile;
    private String privateKey;
    private String impersonatedUser;



    public dsl_GooglecontactSelectAll(
        String value,        String project,        String account,        String dbSrc,        String ptwelveFile,        String privateKey,        String impersonatedUser    ) {
        super(
        );
        this.value = value;
        this.project = project;
        this.account = account;
        this.dbSrc = dbSrc;
        this.ptwelveFile = ptwelveFile;
        this.privateKey = privateKey;
        this.impersonatedUser = impersonatedUser;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getProject() {
        return project;
    }

    public void setProject(String project) {
        this.project = project;
    }
    public String getAccount() {
        return account;
    }

    public void setAccount(String account) {
        this.account = account;
    }
    public String getDbsrc() {
        return dbSrc;
    }

    public void setDbsrc(String dbSrc) {
        this.dbSrc = dbSrc;
    }
    public String getPtwelvefile() {
        return ptwelveFile;
    }

    public void setPtwelvefile(String ptwelveFile) {
        this.ptwelveFile = ptwelveFile;
    }
    public String getPrivatekey() {
        return privateKey;
    }

    public void setPrivatekey(String privateKey) {
        this.privateKey = privateKey;
    }
    public String getImpersonateduser() {
        return impersonatedUser;
    }

    public void setImpersonateduser(String impersonatedUser) {
        this.impersonatedUser = impersonatedUser;
    }


}