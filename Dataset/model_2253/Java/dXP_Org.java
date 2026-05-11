





import java.util.List;
import java.util.ArrayList;

public class dXP_Org extends Base {

    private String name;
    private String type;





    private dXP_OneRoster dxp_oneroster;


    public dXP_Org(
        String name,        String type    ) {
        super(
        );
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public dXP_OneRoster getDxp_oneroster() {
        return dxp_oneroster;
    }

    public void setDxp_oneroster(dXP_OneRoster dxp_oneroster) {
        this.dxp_oneroster = dxp_oneroster;
    }

}