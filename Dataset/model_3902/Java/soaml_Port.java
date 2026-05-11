





import java.util.List;
import java.util.ArrayList;

public class soaml_Port  {

    private String connectorRequired;





    private soaml_Port soaml_port;


    public soaml_Port(
        String connectorRequired    ) {
        this.connectorRequired = connectorRequired;
    }


    public String getConnectorrequired() {
        return connectorRequired;
    }

    public void setConnectorrequired(String connectorRequired) {
        this.connectorRequired = connectorRequired;
    }

    public soaml_Port getSoaml_port() {
        return soaml_port;
    }

    public void setSoaml_port(soaml_Port soaml_port) {
        this.soaml_port = soaml_port;
    }

}