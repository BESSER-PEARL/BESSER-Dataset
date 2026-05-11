





import java.util.List;
import java.util.ArrayList;

public class operators_Operator extends Company {






    private List<operators_ExpansionExperience> operators_expansionexperiences;




    private List<operators_Network> operators_networks;


    public operators_Operator(
    ) {
        super(
        );
        this.operators_expansionexperiences = new ArrayList<>();
        this.operators_networks = new ArrayList<>();
    }

    public operators_Operator(
        ArrayList<operators_ExpansionExperience> operators_expansionexperiences,        ArrayList<operators_Network> operators_networks    ) {
        this.operators_expansionexperiences = operators_expansionexperiences;
        this.operators_networks = operators_networks;
    }


    public List<operators_ExpansionExperience> getOperators_expansionexperiences() {
        return operators_expansionexperiences;
    }

    public void addOperators_expansionexperience(Operators_expansionexperience operators_expansionexperience) {
        this.operators_expansionexperiences.add(operators_expansionexperience);
    }
    public List<operators_Network> getOperators_networks() {
        return operators_networks;
    }

    public void addOperators_network(Operators_network operators_network) {
        this.operators_networks.add(operators_network);
    }

}