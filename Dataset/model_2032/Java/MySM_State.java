





import java.util.List;
import java.util.ArrayList;

public class MySM_State extends Vertex {

    private String name;





    private MySM_Region mysm_region;


    public MySM_State(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MySM_Region getMysm_region() {
        return mysm_region;
    }

    public void setMysm_region(MySM_Region mysm_region) {
        this.mysm_region = mysm_region;
    }

}