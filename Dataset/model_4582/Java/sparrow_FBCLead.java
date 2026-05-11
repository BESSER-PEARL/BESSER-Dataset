





import java.util.List;
import java.util.ArrayList;

public class sparrow_FBCLead extends Action {

    private String accountId;
    private String target;
    private String accessToken;
    private String campaignId;
    private String value;
    private String appSecret;



    public sparrow_FBCLead(
        String accountId,        String target,        String accessToken,        String campaignId,        String value,        String appSecret    ) {
        super(
        );
        this.accountId = accountId;
        this.target = target;
        this.accessToken = accessToken;
        this.campaignId = campaignId;
        this.value = value;
        this.appSecret = appSecret;
    }


    public String getAccountid() {
        return accountId;
    }

    public void setAccountid(String accountId) {
        this.accountId = accountId;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getAccesstoken() {
        return accessToken;
    }

    public void setAccesstoken(String accessToken) {
        this.accessToken = accessToken;
    }
    public String getCampaignid() {
        return campaignId;
    }

    public void setCampaignid(String campaignId) {
        this.campaignId = campaignId;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getAppsecret() {
        return appSecret;
    }

    public void setAppsecret(String appSecret) {
        this.appSecret = appSecret;
    }


}