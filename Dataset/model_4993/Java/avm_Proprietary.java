





import java.util.List;
import java.util.ArrayList;

public class avm_Proprietary extends DistributionRestriction {

    private String Organization;



    public avm_Proprietary(
        String Organization    ) {
        super(
        );
        this.Organization = Organization;
    }


    public String getOrganization() {
        return Organization;
    }

    public void setOrganization(String Organization) {
        this.Organization = Organization;
    }


}