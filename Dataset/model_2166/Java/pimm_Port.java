





import java.util.List;
import java.util.ArrayList;

public class pimm_Port extends PiMMVisitable {

    private String kind;
    private String name;





    private pimm_InterfaceActor pimm_interfaceactor;


    public pimm_Port(
        String kind,        String name    ) {
        super(
        );
        this.kind = kind;
        this.name = name;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pimm_InterfaceActor getPimm_interfaceactor() {
        return pimm_interfaceactor;
    }

    public void setPimm_interfaceactor(pimm_InterfaceActor pimm_interfaceactor) {
        this.pimm_interfaceactor = pimm_interfaceactor;
    }

}