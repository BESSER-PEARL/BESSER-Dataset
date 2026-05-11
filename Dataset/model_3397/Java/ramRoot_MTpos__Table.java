





import java.util.List;
import java.util.ArrayList;

public class ramRoot_MTpos__Table extends MTpos__Element {

    private String MTpos__id;
    private String MTpos__isReserved;



    public ramRoot_MTpos__Table(
        String MTpos__id,        String MTpos__isReserved    ) {
        super(
        );
        this.MTpos__id = MTpos__id;
        this.MTpos__isReserved = MTpos__isReserved;
    }


    public String getMtpos__id() {
        return MTpos__id;
    }

    public void setMtpos__id(String MTpos__id) {
        this.MTpos__id = MTpos__id;
    }
    public String getMtpos__isreserved() {
        return MTpos__isReserved;
    }

    public void setMtpos__isreserved(String MTpos__isReserved) {
        this.MTpos__isReserved = MTpos__isReserved;
    }


}