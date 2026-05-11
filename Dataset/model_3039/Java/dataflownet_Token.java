





import java.util.List;
import java.util.ArrayList;

public class dataflownet_Token  {

    private String value;





    private dataflownet_FiringRule dataflownet_firingrule;




    private dataflownet_Type dataflownet_type;


    public dataflownet_Token(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public dataflownet_FiringRule getDataflownet_firingrule() {
        return dataflownet_firingrule;
    }

    public void setDataflownet_firingrule(dataflownet_FiringRule dataflownet_firingrule) {
        this.dataflownet_firingrule = dataflownet_firingrule;
    }
    public dataflownet_Type getDataflownet_type() {
        return dataflownet_type;
    }

    public void setDataflownet_type(dataflownet_Type dataflownet_type) {
        this.dataflownet_type = dataflownet_type;
    }

}