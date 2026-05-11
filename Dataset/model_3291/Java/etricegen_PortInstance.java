





import java.util.List;
import java.util.ArrayList;

public class etricegen_PortInstance extends InterfaceItemInstance {

    private String kind;





    private etricegen_AbstractInstance etricegen_abstractinstance;


    public etricegen_PortInstance(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public etricegen_AbstractInstance getEtricegen_abstractinstance() {
        return etricegen_abstractinstance;
    }

    public void setEtricegen_abstractinstance(etricegen_AbstractInstance etricegen_abstractinstance) {
        this.etricegen_abstractinstance = etricegen_abstractinstance;
    }

}