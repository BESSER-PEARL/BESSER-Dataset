





import java.util.List;
import java.util.ArrayList;

public class vcml_SetPricingFactor extends SimpleStatement {

    private String location;





    private vcml_Characteristic vcml_characteristic;




    private vcml_Expression vcml_expression;




    private vcml_Expression vcml_expression;


    public vcml_SetPricingFactor(
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
    public vcml_Expression getVcml_expression() {
        return vcml_expression;
    }

    public void setVcml_expression(vcml_Expression vcml_expression) {
        this.vcml_expression = vcml_expression;
    }
    public vcml_Expression getVcml_expression() {
        return vcml_expression;
    }

    public void setVcml_expression(vcml_Expression vcml_expression) {
        this.vcml_expression = vcml_expression;
    }

}