





import java.util.List;
import java.util.ArrayList;

public class Train  {

    private String Cars;
    private String Manufacturer;
    private String Operator;
    private String Power;



    public Train(
        String Cars,        String Manufacturer,        String Operator,        String Power    ) {
        this.Cars = Cars;
        this.Manufacturer = Manufacturer;
        this.Operator = Operator;
        this.Power = Power;
    }


    public String getCars() {
        return Cars;
    }

    public void setCars(String Cars) {
        this.Cars = Cars;
    }
    public String getManufacturer() {
        return Manufacturer;
    }

    public void setManufacturer(String Manufacturer) {
        this.Manufacturer = Manufacturer;
    }
    public String getOperator() {
        return Operator;
    }

    public void setOperator(String Operator) {
        this.Operator = Operator;
    }
    public String getPower() {
        return Power;
    }

    public void setPower(String Power) {
        this.Power = Power;
    }


}