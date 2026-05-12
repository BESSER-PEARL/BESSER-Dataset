





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Filter extends Basic {

    private String value;
    private String token;





    private MavenMaven_FilterSet mavenmaven_filterset;


    public MavenMaven_Filter(
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

    public MavenMaven_FilterSet getMavenmaven_filterset() {
        return mavenmaven_filterset;
    }

    public void setMavenmaven_filterset(MavenMaven_FilterSet mavenmaven_filterset) {
        this.mavenmaven_filterset = mavenmaven_filterset;
    }

}