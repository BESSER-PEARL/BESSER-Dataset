





import java.util.List;
import java.util.ArrayList;

public class camel_requirement_SoftRequirement extends Requirement {

    private float priority;



    public camel_requirement_SoftRequirement(
        float priority    ) {
        super(
        );
        this.priority = priority;
    }


    public float getPriority() {
        return priority;
    }

    public void setPriority(float priority) {
        this.priority = priority;
    }


}