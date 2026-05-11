





import java.util.List;
import java.util.ArrayList;

public class caltrop_Realm  {

    private String key;





    private caltrop_StateVariable caltrop_statevariable;


    public caltrop_Realm(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public caltrop_StateVariable getCaltrop_statevariable() {
        return caltrop_statevariable;
    }

    public void setCaltrop_statevariable(caltrop_StateVariable caltrop_statevariable) {
        this.caltrop_statevariable = caltrop_statevariable;
    }

}