





import java.util.List;
import java.util.ArrayList;

public class farmbot_modeling_BooleanExpression  {

    private int pinNumber;
    private int value;
    private String axe;





    private farmbot_modeling_If farmbot_modeling_if;


    public farmbot_modeling_BooleanExpression(
        int pinNumber,        int value,        String axe    ) {
        this.pinNumber = pinNumber;
        this.value = value;
        this.axe = axe;
    }


    public int getPinnumber() {
        return pinNumber;
    }

    public void setPinnumber(int pinNumber) {
        this.pinNumber = pinNumber;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getAxe() {
        return axe;
    }

    public void setAxe(String axe) {
        this.axe = axe;
    }

    public farmbot_modeling_If getFarmbot_modeling_if() {
        return farmbot_modeling_if;
    }

    public void setFarmbot_modeling_if(farmbot_modeling_If farmbot_modeling_if) {
        this.farmbot_modeling_if = farmbot_modeling_if;
    }

}