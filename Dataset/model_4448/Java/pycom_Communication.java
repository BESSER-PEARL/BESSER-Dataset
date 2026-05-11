





import java.util.List;
import java.util.ArrayList;

public class pycom_Communication extends BoardMember {

    private String type;



    public pycom_Communication(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}