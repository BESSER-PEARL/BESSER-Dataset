





import java.util.List;
import java.util.ArrayList;

public class mt_core_Method  {

    private String name;
    private String return_;



    public mt_core_Method(
        String name,        String return_    ) {
        this.name = name;
        this.return_ = return_;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getReturn_() {
        return return_;
    }

    public void setReturn_(String return_) {
        this.return_ = return_;
    }


}