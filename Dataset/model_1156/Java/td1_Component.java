





import java.util.List;
import java.util.ArrayList;

public class td1_Component  {

    private String Name;
    private int VarSize;
    private int ProcessSize;





    private td1_Port td1_port;




    private List<td1_Port> td1_ports;


    public td1_Component(
        String Name,        int VarSize,        int ProcessSize    ) {
        this.Name = Name;
        this.VarSize = VarSize;
        this.ProcessSize = ProcessSize;
        this.td1_ports = new ArrayList<>();
    }

    public td1_Component(
        String Name,        int VarSize,        int ProcessSize        ArrayList<td1_Port> td1_ports    ) {
        this.Name = Name;
        this.VarSize = VarSize;
        this.ProcessSize = ProcessSize;
        this.td1_ports = td1_ports;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getVarsize() {
        return VarSize;
    }

    public void setVarsize(int VarSize) {
        this.VarSize = VarSize;
    }
    public int getProcesssize() {
        return ProcessSize;
    }

    public void setProcesssize(int ProcessSize) {
        this.ProcessSize = ProcessSize;
    }

    public td1_Port getTd1_port() {
        return td1_port;
    }

    public void setTd1_port(td1_Port td1_port) {
        this.td1_port = td1_port;
    }
    public List<td1_Port> getTd1_ports() {
        return td1_ports;
    }

    public void addTd1_port(Td1_port td1_port) {
        this.td1_ports.add(td1_port);
    }

}