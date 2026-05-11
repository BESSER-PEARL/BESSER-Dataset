





import java.util.List;
import java.util.ArrayList;

public class CarRental2_Check  {

    private int description;





    private CarRental2_TernaryRelationMaintenance carrental2_ternaryrelationmaintenance;




    private List<CarRental2_TernaryRelationMaintenance> carrental2_ternaryrelationmaintenances;


    public CarRental2_Check(
        int description    ) {
        this.description = description;
        this.carrental2_ternaryrelationmaintenances = new ArrayList<>();
    }

    public CarRental2_Check(
        int description        ArrayList<CarRental2_TernaryRelationMaintenance> carrental2_ternaryrelationmaintenances    ) {
        this.description = description;
        this.carrental2_ternaryrelationmaintenances = carrental2_ternaryrelationmaintenances;
    }

    public int getDescription() {
        return description;
    }

    public void setDescription(int description) {
        this.description = description;
    }

    public CarRental2_TernaryRelationMaintenance getCarrental2_ternaryrelationmaintenance() {
        return carrental2_ternaryrelationmaintenance;
    }

    public void setCarrental2_ternaryrelationmaintenance(CarRental2_TernaryRelationMaintenance carrental2_ternaryrelationmaintenance) {
        this.carrental2_ternaryrelationmaintenance = carrental2_ternaryrelationmaintenance;
    }
    public List<CarRental2_TernaryRelationMaintenance> getCarrental2_ternaryrelationmaintenances() {
        return carrental2_ternaryrelationmaintenances;
    }

    public void addCarrental2_ternaryrelationmaintenance(Carrental2_ternaryrelationmaintenance carrental2_ternaryrelationmaintenance) {
        this.carrental2_ternaryrelationmaintenances.add(carrental2_ternaryrelationmaintenance);
    }

}