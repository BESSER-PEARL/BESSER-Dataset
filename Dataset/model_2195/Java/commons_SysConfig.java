





import java.util.List;
import java.util.ArrayList;

public class commons_SysConfig extends Timestamped {

    private String tenantId;



    public commons_SysConfig(
        String tenantId    ) {
        super(
        );
        this.tenantId = tenantId;
    }


    public String getTenantid() {
        return tenantId;
    }

    public void setTenantid(String tenantId) {
        this.tenantId = tenantId;
    }


}