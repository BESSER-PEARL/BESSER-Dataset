





import java.util.List;
import java.util.ArrayList;

public class mission_Mission extends NamedElement {

    private String crs;



    public mission_Mission(
        String crs    ) {
        super(
        );
        this.crs = crs;
    }


    public String getCrs() {
        return crs;
    }

    public void setCrs(String crs) {
        this.crs = crs;
    }


}