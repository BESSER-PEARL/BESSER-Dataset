





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Connector extends Feature {

    private String kind;
    private String contract;
    private String redefinedConnector;
    private String type;



    public UMLModel_Connector(
        String kind,        String contract,        String redefinedConnector,        String type    ) {
        super(
        );
        this.kind = kind;
        this.contract = contract;
        this.redefinedConnector = redefinedConnector;
        this.type = type;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getContract() {
        return contract;
    }

    public void setContract(String contract) {
        this.contract = contract;
    }
    public String getRedefinedconnector() {
        return redefinedConnector;
    }

    public void setRedefinedconnector(String redefinedConnector) {
        this.redefinedConnector = redefinedConnector;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}