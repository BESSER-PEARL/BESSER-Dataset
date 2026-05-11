





import java.util.List;
import java.util.ArrayList;

public class etricegen_OpenBinding  {

    private String path;





    private etricegen_Port etricegen_port;




    private etricegen_WiredStructureClass etricegen_wiredstructureclass;


    public etricegen_OpenBinding(
        String path    ) {
        this.path = path;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }

    public etricegen_Port getEtricegen_port() {
        return etricegen_port;
    }

    public void setEtricegen_port(etricegen_Port etricegen_port) {
        this.etricegen_port = etricegen_port;
    }
    public etricegen_WiredStructureClass getEtricegen_wiredstructureclass() {
        return etricegen_wiredstructureclass;
    }

    public void setEtricegen_wiredstructureclass(etricegen_WiredStructureClass etricegen_wiredstructureclass) {
        this.etricegen_wiredstructureclass = etricegen_wiredstructureclass;
    }

}