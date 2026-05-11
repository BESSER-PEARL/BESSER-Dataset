





import java.util.List;
import java.util.ArrayList;

public class netModel_Client extends Declaration {

    private String baseUrl;



    public netModel_Client(
        String baseUrl    ) {
        super(
        );
        this.baseUrl = baseUrl;
    }


    public String getBaseurl() {
        return baseUrl;
    }

    public void setBaseurl(String baseUrl) {
        this.baseUrl = baseUrl;
    }


}