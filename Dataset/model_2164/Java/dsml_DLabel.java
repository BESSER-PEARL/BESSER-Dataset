





import java.util.List;
import java.util.ArrayList;

public class dsml_DLabel  {

    private String name;





    private dsml_DNode dsml_dnode;


    public dsml_DLabel(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsml_DNode getDsml_dnode() {
        return dsml_dnode;
    }

    public void setDsml_dnode(dsml_DNode dsml_dnode) {
        this.dsml_dnode = dsml_dnode;
    }

}