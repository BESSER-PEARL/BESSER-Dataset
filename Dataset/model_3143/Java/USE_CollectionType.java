





import java.util.List;
import java.util.ArrayList;

public class USE_CollectionType extends Type {

    private String type;





    private USE_Type use_type;


    public USE_CollectionType(
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

    public USE_Type getUse_type() {
        return use_type;
    }

    public void setUse_type(USE_Type use_type) {
        this.use_type = use_type;
    }

}