





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsFeature  {

    private String name;





    private rdbms_RdbmsConfiguration rdbms_rdbmsconfiguration;


    public rdbms_RdbmsFeature(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rdbms_RdbmsConfiguration getRdbms_rdbmsconfiguration() {
        return rdbms_rdbmsconfiguration;
    }

    public void setRdbms_rdbmsconfiguration(rdbms_RdbmsConfiguration rdbms_rdbmsconfiguration) {
        this.rdbms_rdbmsconfiguration = rdbms_rdbmsconfiguration;
    }

}