





import java.util.List;
import java.util.ArrayList;

public class dsl_SmsLeadSms extends Action {

    private String account;
    private String privateKey;
    private String dbSrc;
    private String dryrunNumber;
    private String value;
    private String sender;
    private String url;



    public dsl_SmsLeadSms(
        String account,        String privateKey,        String dbSrc,        String dryrunNumber,        String value,        String sender,        String url    ) {
        super(
        );
        this.account = account;
        this.privateKey = privateKey;
        this.dbSrc = dbSrc;
        this.dryrunNumber = dryrunNumber;
        this.value = value;
        this.sender = sender;
        this.url = url;
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
    public String getDbsrc() {
        return dbSrc;
    }

    public void setDbsrc(String dbSrc) {
        this.dbSrc = dbSrc;
    }
    public String getDryrunnumber() {
        return dryrunNumber;
    }

    public void setDryrunnumber(String dryrunNumber) {
        this.dryrunNumber = dryrunNumber;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getSender() {
        return sender;
    }

    public void setSender(String sender) {
        this.sender = sender;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }


}