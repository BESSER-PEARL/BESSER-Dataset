





import java.util.List;
import java.util.ArrayList;

public class dsl_ClickSendSms extends Action {

    private String securityKey;
    private String target;
    private String userid;
    private String value;



    public dsl_ClickSendSms(
        String securityKey,        String target,        String userid,        String value    ) {
        super(
        );
        this.securityKey = securityKey;
        this.target = target;
        this.userid = userid;
        this.value = value;
    }


    public String getSecuritykey() {
        return securityKey;
    }

    public void setSecuritykey(String securityKey) {
        this.securityKey = securityKey;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getUserid() {
        return userid;
    }

    public void setUserid(String userid) {
        this.userid = userid;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}