





import java.util.List;
import java.util.ArrayList;

public class SMVC_EntityController extends Controller {

    private String returnOKURL;
    private String returnKOURL;



    public SMVC_EntityController(
        String returnOKURL,        String returnKOURL    ) {
        super(
        );
        this.returnOKURL = returnOKURL;
        this.returnKOURL = returnKOURL;
    }


    public String getReturnokurl() {
        return returnOKURL;
    }

    public void setReturnokurl(String returnOKURL) {
        this.returnOKURL = returnOKURL;
    }
    public String getReturnkourl() {
        return returnKOURL;
    }

    public void setReturnkourl(String returnKOURL) {
        this.returnKOURL = returnKOURL;
    }


}