





import java.util.List;
import java.util.ArrayList;

public class RestServices  {

    private String base_url;



    public RestServices(
        String base_url    ) {
        this.base_url = base_url;
    }


    public String getBase_url() {
        return base_url;
    }

    public void setBase_url(String base_url) {
        this.base_url = base_url;
    }


}