





import java.util.List;
import java.util.ArrayList;

public class CarRental2_Check  {

    private String description;





    private List<CarRental2_ServiceDepot> carrental2_servicedepots;


    public CarRental2_Check(
        String description    ) {
        this.description = description;
        this.carrental2_servicedepots = new ArrayList<>();
    }

    public CarRental2_Check(
        String description        ArrayList<CarRental2_ServiceDepot> carrental2_servicedepots    ) {
        this.description = description;
        this.carrental2_servicedepots = carrental2_servicedepots;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<CarRental2_ServiceDepot> getCarrental2_servicedepots() {
        return carrental2_servicedepots;
    }

    public void addCarrental2_servicedepot(Carrental2_servicedepot carrental2_servicedepot) {
        this.carrental2_servicedepots.add(carrental2_servicedepot);
    }

}