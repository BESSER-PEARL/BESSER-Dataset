





import java.util.List;
import java.util.ArrayList;

public class ocl_constraints_OclInvariant extends LocatedElement {

    private String description;
    private String name;



    public ocl_constraints_OclInvariant(
        String description,        String name    ) {
        super(
        );
        this.description = description;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}