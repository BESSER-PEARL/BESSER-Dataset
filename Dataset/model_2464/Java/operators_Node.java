





import java.util.List;
import java.util.ArrayList;

public class operators_Node  {

    private String nodeID;





    private operators_Function operators_function;




    private List<operators_Equipment> operators_equipments;




    private List<operators_Function> operators_functions;




    private operators_Network operators_network;




    private operators_Person operators_person;




    private operators_Equipment operators_equipment;


    public operators_Node(
        String nodeID    ) {
        this.nodeID = nodeID;
        this.operators_equipments = new ArrayList<>();
        this.operators_functions = new ArrayList<>();
    }

    public operators_Node(
        String nodeID        ArrayList<operators_Equipment> operators_equipments,        ArrayList<operators_Function> operators_functions    ) {
        this.nodeID = nodeID;
        this.operators_equipments = operators_equipments;
        this.operators_functions = operators_functions;
    }

    public String getNodeid() {
        return nodeID;
    }

    public void setNodeid(String nodeID) {
        this.nodeID = nodeID;
    }

    public operators_Function getOperators_function() {
        return operators_function;
    }

    public void setOperators_function(operators_Function operators_function) {
        this.operators_function = operators_function;
    }
    public List<operators_Equipment> getOperators_equipments() {
        return operators_equipments;
    }

    public void addOperators_equipment(Operators_equipment operators_equipment) {
        this.operators_equipments.add(operators_equipment);
    }
    public List<operators_Function> getOperators_functions() {
        return operators_functions;
    }

    public void addOperators_function(Operators_function operators_function) {
        this.operators_functions.add(operators_function);
    }
    public operators_Network getOperators_network() {
        return operators_network;
    }

    public void setOperators_network(operators_Network operators_network) {
        this.operators_network = operators_network;
    }
    public operators_Person getOperators_person() {
        return operators_person;
    }

    public void setOperators_person(operators_Person operators_person) {
        this.operators_person = operators_person;
    }
    public operators_Equipment getOperators_equipment() {
        return operators_equipment;
    }

    public void setOperators_equipment(operators_Equipment operators_equipment) {
        this.operators_equipment = operators_equipment;
    }

}