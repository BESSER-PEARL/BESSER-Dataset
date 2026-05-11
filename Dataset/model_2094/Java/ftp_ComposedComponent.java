





import java.util.List;
import java.util.ArrayList;

public class ftp_ComposedComponent extends Component {






    private List<ftp_Port> ftp_ports;


    public ftp_ComposedComponent(
    ) {
        super(
        );
        this.ftp_ports = new ArrayList<>();
    }

    public ftp_ComposedComponent(
        ArrayList<ftp_Port> ftp_ports    ) {
        this.ftp_ports = ftp_ports;
    }


    public List<ftp_Port> getFtp_ports() {
        return ftp_ports;
    }

    public void addFtp_port(Ftp_port ftp_port) {
        this.ftp_ports.add(ftp_port);
    }

}