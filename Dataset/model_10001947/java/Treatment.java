





import java.util.List;
import java.util.ArrayList;

public class Treatment  {

    private String disease;
    private String id;



    public Treatment(
        String disease,        String id    ) {
        this.disease = disease;
        this.id = id;
    }


    public String getDisease() {
        return disease;
    }

    public void setDisease(String disease) {
        this.disease = disease;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}