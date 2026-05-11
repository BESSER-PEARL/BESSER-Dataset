





import java.util.List;
import java.util.ArrayList;

public class vcml_SumParts extends Expression {

    private String location;





    private vcml_Characteristic vcml_characteristic;


    public vcml_SumParts(
        String location    ) {
        super(
        );
        this.location = location;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public vcml_Characteristic getVcml_characteristic() {
        return vcml_characteristic;
    }

    public void setVcml_characteristic(vcml_Characteristic vcml_characteristic) {
        this.vcml_characteristic = vcml_characteristic;
    }

}