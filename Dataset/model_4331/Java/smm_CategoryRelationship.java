





import java.util.List;
import java.util.ArrayList;

public class smm_CategoryRelationship extends SmmRelationship {

    private String name;



    public smm_CategoryRelationship(
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