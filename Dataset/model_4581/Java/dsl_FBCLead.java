





import java.util.List;
import java.util.ArrayList;

public class dsl_FBCLead extends Action {

    private String accountId;
    private String accessToken;
    private String appSecret;
    private String target;
    private String value;
    private String campaignId;



    public dsl_FBCLead(
        String accountId,        String accessToken,        String appSecret,        String target,        String value,        String campaignId    ) {
        super(
        );
        this.accountId = accountId;
        this.accessToken = accessToken;
        this.appSecret = appSecret;
        this.target = target;
        this.value = value;
        this.campaignId = campaignId;
    }


    public String getAccountid() {
        return accountId;
    }

    public void setAccountid(String accountId) {
        this.accountId = accountId;
    }
    public String getAccesstoken() {
        return accessToken;
    }

    public void setAccesstoken(String accessToken) {
        this.accessToken = accessToken;
    }
    public String getAppsecret() {
        return appSecret;
    }

    public void setAppsecret(String appSecret) {
        this.appSecret = appSecret;
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
    public String getCampaignid() {
        return campaignId;
    }

    public void setCampaignid(String campaignId) {
        this.campaignId = campaignId;
    }


}