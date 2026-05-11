





import java.util.List;
import java.util.ArrayList;

public class p2_IRequiredCapability extends IRequirement {

    private String range;
    private String namespace;
    private String name;





    private p2_IRequirementChange p2_irequirementchange;




    private p2_IRequirementChange p2_irequirementchange;


    public p2_IRequiredCapability(
        String range,        String namespace,        String name    ) {
        super(
        );
        this.range = range;
        this.namespace = namespace;
        this.name = name;
    }


    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public p2_IRequirementChange getP2_irequirementchange() {
        return p2_irequirementchange;
    }

    public void setP2_irequirementchange(p2_IRequirementChange p2_irequirementchange) {
        this.p2_irequirementchange = p2_irequirementchange;
    }
    public p2_IRequirementChange getP2_irequirementchange() {
        return p2_irequirementchange;
    }

    public void setP2_irequirementchange(p2_IRequirementChange p2_irequirementchange) {
        this.p2_irequirementchange = p2_irequirementchange;
    }

}