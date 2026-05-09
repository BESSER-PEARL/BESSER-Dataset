





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ProtocolConformance extends DirectedRelationship {

    private String specificMachine;
    private String generalMachine;



    public UMLModel_ProtocolConformance(
        String specificMachine,        String generalMachine    ) {
        super(
        );
        this.specificMachine = specificMachine;
        this.generalMachine = generalMachine;
    }


    public String getSpecificmachine() {
        return specificMachine;
    }

    public void setSpecificmachine(String specificMachine) {
        this.specificMachine = specificMachine;
    }
    public String getGeneralmachine() {
        return generalMachine;
    }

    public void setGeneralmachine(String generalMachine) {
        this.generalMachine = generalMachine;
    }


}