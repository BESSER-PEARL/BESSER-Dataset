





import java.util.List;
import java.util.ArrayList;

public class model_MPrimitiveTypeReference extends AbstractMTypeReference {

    private String type;



    public model_MPrimitiveTypeReference(
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