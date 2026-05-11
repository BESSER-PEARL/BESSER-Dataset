





import java.util.List;
import java.util.ArrayList;

public class iOI_Company  {

    private String name;





    private iOI_Model ioi_model;


    public iOI_Company(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iOI_Model getIoi_model() {
        return ioi_model;
    }

    public void setIoi_model(iOI_Model ioi_model) {
        this.ioi_model = ioi_model;
    }

}