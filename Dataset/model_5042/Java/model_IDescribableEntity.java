





import java.util.List;
import java.util.ArrayList;

public class model_IDescribableEntity extends IEntity {

    private String description;



    public model_IDescribableEntity(
        String description    ) {
        super(
        );
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}