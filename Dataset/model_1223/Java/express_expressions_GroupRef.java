





import java.util.List;
import java.util.ArrayList;

public class express_expressions_GroupRef extends Selector {

    private String id;





    private SingleEntityType singleentitytype;


    public express_expressions_GroupRef(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public SingleEntityType getSingleentitytype() {
        return singleentitytype;
    }

    public void setSingleentitytype(SingleEntityType singleentitytype) {
        this.singleentitytype = singleentitytype;
    }

}