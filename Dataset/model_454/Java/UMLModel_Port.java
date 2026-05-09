





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Port extends Property {

    private String isService;
    private String required;
    private String protocol;
    private String redefinedPort;
    private String provided;
    private String isBehavior;



    public UMLModel_Port(
        String isService,        String required,        String protocol,        String redefinedPort,        String provided,        String isBehavior    ) {
        super(
        );
        this.isService = isService;
        this.required = required;
        this.protocol = protocol;
        this.redefinedPort = redefinedPort;
        this.provided = provided;
        this.isBehavior = isBehavior;
    }


    public String getIsservice() {
        return isService;
    }

    public void setIsservice(String isService) {
        this.isService = isService;
    }
    public String getRequired() {
        return required;
    }

    public void setRequired(String required) {
        this.required = required;
    }
    public String getProtocol() {
        return protocol;
    }

    public void setProtocol(String protocol) {
        this.protocol = protocol;
    }
    public String getRedefinedport() {
        return redefinedPort;
    }

    public void setRedefinedport(String redefinedPort) {
        this.redefinedPort = redefinedPort;
    }
    public String getProvided() {
        return provided;
    }

    public void setProvided(String provided) {
        this.provided = provided;
    }
    public String getIsbehavior() {
        return isBehavior;
    }

    public void setIsbehavior(String isBehavior) {
        this.isBehavior = isBehavior;
    }


}