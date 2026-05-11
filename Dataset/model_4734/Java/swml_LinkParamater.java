





import java.util.List;
import java.util.ArrayList;

public class swml_LinkParamater  {

    private String Parameter;





    private swml_Links swml_links;


    public swml_LinkParamater(
        String Parameter    ) {
        this.Parameter = Parameter;
    }


    public String getParameter() {
        return Parameter;
    }

    public void setParameter(String Parameter) {
        this.Parameter = Parameter;
    }

    public swml_Links getSwml_links() {
        return swml_links;
    }

    public void setSwml_links(swml_Links swml_links) {
        this.swml_links = swml_links;
    }

}