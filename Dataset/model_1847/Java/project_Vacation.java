





import java.util.List;
import java.util.ArrayList;

public class project_Vacation extends Property, ResourceAttribute {

    private String name;



    public project_Vacation(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}