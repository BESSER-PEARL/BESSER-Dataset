





import java.util.List;
import java.util.ArrayList;

public class dsl_FBFormDownload extends Action {

    private String appSecret;
    private String accountId;
    private String formId;
    private String target;
    private String value;
    private String accessToken;



    public dsl_FBFormDownload(
        String appSecret,        String accountId,        String formId,        String target,        String value,        String accessToken    ) {
        super(
        );
        this.appSecret = appSecret;
        this.accountId = accountId;
        this.formId = formId;
        this.target = target;
        this.value = value;
        this.accessToken = accessToken;
    }


    public String getAppsecret() {
        return appSecret;
    }

    public void setAppsecret(String appSecret) {
        this.appSecret = appSecret;
    }
    public String getAccountid() {
        return accountId;
    }

    public void setAccountid(String accountId) {
        this.accountId = accountId;
    }
    public String getFormid() {
        return formId;
    }

    public void setFormid(String formId) {
        this.formId = formId;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getAccesstoken() {
        return accessToken;
    }

    public void setAccesstoken(String accessToken) {
        this.accessToken = accessToken;
    }


}