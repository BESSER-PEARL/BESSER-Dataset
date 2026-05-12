





import java.util.List;
import java.util.ArrayList;

public class Ant_Filter extends Basic {

    private String value;
    private String token;



    public Ant_Filter(
        String value,        String token    ) {
        super(
        );
        this.value = value;
        this.token = token;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }


}