





import java.util.List;
import java.util.ArrayList;

public class express_ExpressConcept  {

    private String name;





    private express_SelectType express_selecttype;


    public express_ExpressConcept(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public express_SelectType getExpress_selecttype() {
        return express_selecttype;
    }

    public void setExpress_selecttype(express_SelectType express_selecttype) {
        this.express_selecttype = express_selecttype;
    }

}