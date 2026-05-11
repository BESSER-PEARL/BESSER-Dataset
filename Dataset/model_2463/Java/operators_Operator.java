





import java.util.List;
import java.util.ArrayList;

public class operators_Operator extends Company {






    private List<operators_Network> operators_networks;




    private List<operators_ExpansionExperience> operators_expansionexperiences;


    public operators_Operator(
    ) {
        super(
        );
        this.operators_networks = new ArrayList<>();
        this.operators_expansionexperiences = new ArrayList<>();
    }

    public operators_Operator(
        ArrayList<operators_Network> operators_networks,        ArrayList<operators_ExpansionExperience> operators_expansionexperiences    ) {
        this.operators_networks = operators_networks;
        this.operators_expansionexperiences = operators_expansionexperiences;
    }


    public List<operators_Network> getOperators_networks() {
        return operators_networks;
    }

    public void addOperators_network(Operators_network operators_network) {
        this.operators_networks.add(operators_network);
    }
    public List<operators_ExpansionExperience> getOperators_expansionexperiences() {
        return operators_expansionexperiences;
    }

    public void addOperators_expansionexperience(Operators_expansionexperience operators_expansionexperience) {
        this.operators_expansionexperiences.add(operators_expansionexperience);
    }

}