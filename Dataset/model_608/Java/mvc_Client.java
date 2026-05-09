





import java.util.List;
import java.util.ArrayList;

public class mvc_Client extends Model {

    private String nameservice;





    private mvc_Method mvc_method;


    public mvc_Client(
        String nameservice    ) {
        super(
        );
        this.nameservice = nameservice;
    }


    public String getNameservice() {
        return nameservice;
    }

    public void setNameservice(String nameservice) {
        this.nameservice = nameservice;
    }

    public mvc_Method getMvc_method() {
        return mvc_method;
    }

    public void setMvc_method(mvc_Method mvc_method) {
        this.mvc_method = mvc_method;
    }

}