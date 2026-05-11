





import java.util.List;
import java.util.ArrayList;

public class CarRental2_ServiceDepot  {

    private int location;





    private List<CarRental2_TernaryRelationMaintenance> carrental2_ternaryrelationmaintenances;




    private CarRental2_TernaryRelationMaintenance carrental2_ternaryrelationmaintenance;


    public CarRental2_ServiceDepot(
        int location    ) {
        this.location = location;
        this.carrental2_ternaryrelationmaintenances = new ArrayList<>();
    }

    public CarRental2_ServiceDepot(
        int location        ArrayList<CarRental2_TernaryRelationMaintenance> carrental2_ternaryrelationmaintenances    ) {
        this.location = location;
        this.carrental2_ternaryrelationmaintenances = carrental2_ternaryrelationmaintenances;
    }

    public int getLocation() {
        return location;
    }

    public void setLocation(int location) {
        this.location = location;
    }

    public List<CarRental2_TernaryRelationMaintenance> getCarrental2_ternaryrelationmaintenances() {
        return carrental2_ternaryrelationmaintenances;
    }

    public void addCarrental2_ternaryrelationmaintenance(Carrental2_ternaryrelationmaintenance carrental2_ternaryrelationmaintenance) {
        this.carrental2_ternaryrelationmaintenances.add(carrental2_ternaryrelationmaintenance);
    }
    public CarRental2_TernaryRelationMaintenance getCarrental2_ternaryrelationmaintenance() {
        return carrental2_ternaryrelationmaintenance;
    }

    public void setCarrental2_ternaryrelationmaintenance(CarRental2_TernaryRelationMaintenance carrental2_ternaryrelationmaintenance) {
        this.carrental2_ternaryrelationmaintenance = carrental2_ternaryrelationmaintenance;
    }

}