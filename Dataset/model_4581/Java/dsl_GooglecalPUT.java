





import java.util.List;
import java.util.ArrayList;

public class dsl_GooglecalPUT extends Action {

    private String account;
    private String dbSrc;
    private String value;
    private String project;
    private String impersonatedUser;
    private String privateKey;
    private String ptwelveFile;



    public dsl_GooglecalPUT(
        String account,        String dbSrc,        String value,        String project,        String impersonatedUser,        String privateKey,        String ptwelveFile    ) {
        super(
        );
        this.account = account;
        this.dbSrc = dbSrc;
        this.value = value;
        this.project = project;
        this.impersonatedUser = impersonatedUser;
        this.privateKey = privateKey;
        this.ptwelveFile = ptwelveFile;
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
    public String getImpersonateduser() {
        return impersonatedUser;
    }

    public void setImpersonateduser(String impersonatedUser) {
        this.impersonatedUser = impersonatedUser;
    }
    public String getPrivatekey() {
        return privateKey;
    }

    public void setPrivatekey(String privateKey) {
        this.privateKey = privateKey;
    }
    public String getPtwelvefile() {
        return ptwelveFile;
    }

    public void setPtwelvefile(String ptwelveFile) {
        this.ptwelveFile = ptwelveFile;
    }


}