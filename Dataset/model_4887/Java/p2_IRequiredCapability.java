





import java.util.List;
import java.util.ArrayList;

public class p2_IRequiredCapability extends IRequirement {

    private String range;
    private String name;
    private String namespace;





    private p2_IRequirementChange p2_irequirementchange;




    private p2_IRequirementChange p2_irequirementchange;


    public p2_IRequiredCapability(
        String range,        String name,        String namespace    ) {
        super(
        );
        this.range = range;
        this.name = name;
        this.namespace = namespace;
    }


    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
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