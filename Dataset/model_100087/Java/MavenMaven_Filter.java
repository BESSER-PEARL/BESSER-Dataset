





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Filter extends Basic {

    private String token;
    private String value;



    public MavenMaven_Filter(
        String token,        String value    ) {
        super(
        );
        this.token = token;
        this.value = value;
    }


    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}