





import java.util.List;
import java.util.ArrayList;

public class dsl_SendMail extends Action {

    private String dbSrc;
    private String impersonatedUser;
    private String dryrunMail;
    private String privateKey;
    private String value;



    public dsl_SendMail(
        String dbSrc,        String impersonatedUser,        String dryrunMail,        String privateKey,        String value    ) {
        super(
        );
        this.dbSrc = dbSrc;
        this.impersonatedUser = impersonatedUser;
        this.dryrunMail = dryrunMail;
        this.privateKey = privateKey;
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
    public String getDryrunmail() {
        return dryrunMail;
    }

    public void setDryrunmail(String dryrunMail) {
        this.dryrunMail = dryrunMail;
    }
    public String getPrivatekey() {
        return privateKey;
    }

    public void setPrivatekey(String privateKey) {
        this.privateKey = privateKey;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}