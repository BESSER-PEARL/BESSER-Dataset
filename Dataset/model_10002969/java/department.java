





import java.util.List;
import java.util.ArrayList;

public class department  {

    private String depart_id;
    private String loacation;



    public department(
        String depart_id,        String loacation    ) {
        this.depart_id = depart_id;
        this.loacation = loacation;
    }


    public String getDepart_id() {
        return depart_id;
    }

    public void setDepart_id(String depart_id) {
        this.depart_id = depart_id;
    }
    public String getLoacation() {
        return loacation;
    }

    public void setLoacation(String loacation) {
        this.loacation = loacation;
    }


}