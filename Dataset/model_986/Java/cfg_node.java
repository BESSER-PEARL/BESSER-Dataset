





import java.util.List;
import java.util.ArrayList;

public class cfg_node  {

    private String name;





    private cfg_cfg cfg_cfg;


    public cfg_node(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cfg_cfg getCfg_cfg() {
        return cfg_cfg;
    }

    public void setCfg_cfg(cfg_cfg cfg_cfg) {
        this.cfg_cfg = cfg_cfg;
    }

}