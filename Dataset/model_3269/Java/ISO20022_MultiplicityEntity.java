





import java.util.List;
import java.util.ArrayList;

public class ISO20022_MultiplicityEntity  {

    private String minOccurs;
    private String maxOccurs;



    public ISO20022_MultiplicityEntity(
        String minOccurs,        String maxOccurs    ) {
        this.minOccurs = minOccurs;
        this.maxOccurs = maxOccurs;
    }


    public String getMinoccurs() {
        return minOccurs;
    }

    public void setMinoccurs(String minOccurs) {
        this.minOccurs = minOccurs;
    }
    public String getMaxoccurs() {
        return maxOccurs;
    }

    public void setMaxoccurs(String maxOccurs) {
        this.maxOccurs = maxOccurs;
    }


}