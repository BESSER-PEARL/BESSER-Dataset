





import java.util.List;
import java.util.ArrayList;

public class effbd2_ItemContent  {

    private String id;





    private effbd2_Transformed effbd2_transformed;


    public effbd2_ItemContent(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public effbd2_Transformed getEffbd2_transformed() {
        return effbd2_transformed;
    }

    public void setEffbd2_transformed(effbd2_Transformed effbd2_transformed) {
        this.effbd2_transformed = effbd2_transformed;
    }

}