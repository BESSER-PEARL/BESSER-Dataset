





import java.util.List;
import java.util.ArrayList;

public class EA_Model_Travel  {






    private EA_Model_Traveler ea_model_traveler;




    private List<EA_Model_Traveler> ea_model_travelers;


    public EA_Model_Travel(
    ) {
        this.ea_model_travelers = new ArrayList<>();
    }

    public EA_Model_Travel(
        ArrayList<EA_Model_Traveler> ea_model_travelers    ) {
        this.ea_model_travelers = ea_model_travelers;
    }


    public EA_Model_Traveler getEa_model_traveler() {
        return ea_model_traveler;
    }

    public void setEa_model_traveler(EA_Model_Traveler ea_model_traveler) {
        this.ea_model_traveler = ea_model_traveler;
    }
    public List<EA_Model_Traveler> getEa_model_travelers() {
        return ea_model_travelers;
    }

    public void addEa_model_traveler(Ea_model_traveler ea_model_traveler) {
        this.ea_model_travelers.add(ea_model_traveler);
    }

}