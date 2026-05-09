





import java.util.List;
import java.util.ArrayList;

public class pycom_System  {






    private List<pycom_Server> pycom_servers;


    public pycom_System(
    ) {
        this.pycom_servers = new ArrayList<>();
    }

    public pycom_System(
        ArrayList<pycom_Server> pycom_servers    ) {
        this.pycom_servers = pycom_servers;
    }


    public List<pycom_Server> getPycom_servers() {
        return pycom_servers;
    }

    public void addPycom_server(Pycom_server pycom_server) {
        this.pycom_servers.add(pycom_server);
    }

}