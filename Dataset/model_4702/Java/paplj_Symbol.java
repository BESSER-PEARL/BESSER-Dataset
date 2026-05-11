





import java.util.List;
import java.util.ArrayList;

public class paplj_Symbol  {

    private String name;





    private paplj_Type paplj_type;


    public paplj_Symbol(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public paplj_Type getPaplj_type() {
        return paplj_type;
    }

    public void setPaplj_type(paplj_Type paplj_type) {
        this.paplj_type = paplj_type;
    }

}