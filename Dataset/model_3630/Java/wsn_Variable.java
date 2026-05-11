





import java.util.List;
import java.util.ArrayList;

public class wsn_Variable  {

    private float initial;
    private boolean signed;
    private String type;





    private wsn_Data wsn_data;


    public wsn_Variable(
        float initial,        boolean signed,        String type    ) {
        this.initial = initial;
        this.signed = signed;
        this.type = type;
    }


    public float getInitial() {
        return initial;
    }

    public void setInitial(float initial) {
        this.initial = initial;
    }
    public boolean getSigned() {
        return signed;
    }

    public void setSigned(boolean signed) {
        this.signed = signed;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public wsn_Data getWsn_data() {
        return wsn_data;
    }

    public void setWsn_data(wsn_Data wsn_data) {
        this.wsn_data = wsn_data;
    }

}