





import java.util.List;
import java.util.ArrayList;

public class iotsystem_DigitalArtifact extends NamedElement {






    private List<iotsystem_Rule> iotsystem_rules;




    private iotsystem_IotSystem iotsystem_iotsystem;


    public iotsystem_DigitalArtifact(
    ) {
        super(
        );
        this.iotsystem_rules = new ArrayList<>();
    }

    public iotsystem_DigitalArtifact(
        ArrayList<iotsystem_Rule> iotsystem_rules    ) {
        this.iotsystem_rules = iotsystem_rules;
    }


    public List<iotsystem_Rule> getIotsystem_rules() {
        return iotsystem_rules;
    }

    public void addIotsystem_rule(Iotsystem_rule iotsystem_rule) {
        this.iotsystem_rules.add(iotsystem_rule);
    }
    public iotsystem_IotSystem getIotsystem_iotsystem() {
        return iotsystem_iotsystem;
    }

    public void setIotsystem_iotsystem(iotsystem_IotSystem iotsystem_iotsystem) {
        this.iotsystem_iotsystem = iotsystem_iotsystem;
    }

}