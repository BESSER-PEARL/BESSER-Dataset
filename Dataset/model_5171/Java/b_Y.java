





import java.util.List;
import java.util.ArrayList;

public class b_Y  {

    private String info;
    private String label;





    private b_Model b_model;


    public b_Y(
        String info,        String label    ) {
        this.info = info;
        this.label = label;
    }


    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public b_Model getB_model() {
        return b_model;
    }

    public void setB_model(b_Model b_model) {
        this.b_model = b_model;
    }

}