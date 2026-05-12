





import java.util.List;
import java.util.ArrayList;

public class ErrorCode  {

    private int domain;
    private int subdomain;
    private int reason;
    private int tier;



    public ErrorCode(
        int domain,        int subdomain,        int reason,        int tier    ) {
        this.domain = domain;
        this.subdomain = subdomain;
        this.reason = reason;
        this.tier = tier;
    }


    public int getDomain() {
        return domain;
    }

    public void setDomain(int domain) {
        this.domain = domain;
    }
    public int getSubdomain() {
        return subdomain;
    }

    public void setSubdomain(int subdomain) {
        this.subdomain = subdomain;
    }
    public int getReason() {
        return reason;
    }

    public void setReason(int reason) {
        this.reason = reason;
    }
    public int getTier() {
        return tier;
    }

    public void setTier(int tier) {
        this.tier = tier;
    }


}