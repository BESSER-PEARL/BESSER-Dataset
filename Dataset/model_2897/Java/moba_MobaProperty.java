





import java.util.List;
import java.util.ArrayList;

public class moba_MobaProperty  {

    private String key;
    private String value;
    private String valueString;
    private String keyString;





    private moba_MobaPropertiesAble moba_mobapropertiesable;




    private moba_MobaConstant moba_mobaconstant;




    private moba_MobaConstant moba_mobaconstant;


    public moba_MobaProperty(
        String key,        String value,        String valueString,        String keyString    ) {
        this.key = key;
        this.value = value;
        this.valueString = valueString;
        this.keyString = keyString;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getValuestring() {
        return valueString;
    }

    public void setValuestring(String valueString) {
        this.valueString = valueString;
    }
    public String getKeystring() {
        return keyString;
    }

    public void setKeystring(String keyString) {
        this.keyString = keyString;
    }

    public moba_MobaPropertiesAble getMoba_mobapropertiesable() {
        return moba_mobapropertiesable;
    }

    public void setMoba_mobapropertiesable(moba_MobaPropertiesAble moba_mobapropertiesable) {
        this.moba_mobapropertiesable = moba_mobapropertiesable;
    }
    public moba_MobaConstant getMoba_mobaconstant() {
        return moba_mobaconstant;
    }

    public void setMoba_mobaconstant(moba_MobaConstant moba_mobaconstant) {
        this.moba_mobaconstant = moba_mobaconstant;
    }
    public moba_MobaConstant getMoba_mobaconstant() {
        return moba_mobaconstant;
    }

    public void setMoba_mobaconstant(moba_MobaConstant moba_mobaconstant) {
        this.moba_mobaconstant = moba_mobaconstant;
    }

}