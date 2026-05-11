





import java.util.List;
import java.util.ArrayList;

public class mt_core_Method  {

    private String return_;
    private String name;



    public mt_core_Method(
        String return_,        String name    ) {
        this.return_ = return_;
        this.name = name;
    }


    public String getReturn_() {
        return return_;
    }

    public void setReturn_(String return_) {
        this.return_ = return_;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}