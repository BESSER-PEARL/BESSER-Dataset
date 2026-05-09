





import java.util.List;
import java.util.ArrayList;

public class eTJ_Account extends Property, AccountAttribute {

    private String id;
    private String name;





    private eTJ_SupplementAccount etj_supplementaccount;


    public eTJ_Account(
        String id,        String name    ) {
        super(
        );
        this.id = id;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eTJ_SupplementAccount getEtj_supplementaccount() {
        return etj_supplementaccount;
    }

    public void setEtj_supplementaccount(eTJ_SupplementAccount etj_supplementaccount) {
        this.etj_supplementaccount = etj_supplementaccount;
    }

}