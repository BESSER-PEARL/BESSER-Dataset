





import java.util.List;
import java.util.ArrayList;

public class netModel_Declaration  {

    private String name;





    private netModel_Model netmodel_model;


    public netModel_Declaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public netModel_Model getNetmodel_model() {
        return netmodel_model;
    }

    public void setNetmodel_model(netModel_Model netmodel_model) {
        this.netmodel_model = netmodel_model;
    }

}