





import java.util.List;
import java.util.ArrayList;

public class moba_MobaFriend  {

    private String value;
    private String valueString;





    private moba_MobaConstant moba_mobaconstant;


    public moba_MobaFriend(
        String value,        String valueString    ) {
        this.value = value;
        this.valueString = valueString;
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

    public moba_MobaConstant getMoba_mobaconstant() {
        return moba_mobaconstant;
    }

    public void setMoba_mobaconstant(moba_MobaConstant moba_mobaconstant) {
        this.moba_mobaconstant = moba_mobaconstant;
    }

}