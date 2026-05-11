





import java.util.List;
import java.util.ArrayList;

public class aadl2_AccessConnection extends Connection {

    private String accessCategory;



    public aadl2_AccessConnection(
        String accessCategory    ) {
        super(
        );
        this.accessCategory = accessCategory;
    }


    public String getAccesscategory() {
        return accessCategory;
    }

    public void setAccesscategory(String accessCategory) {
        this.accessCategory = accessCategory;
    }


}