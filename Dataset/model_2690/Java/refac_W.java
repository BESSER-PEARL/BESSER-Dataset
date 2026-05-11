





import java.util.List;
import java.util.ArrayList;

public class refac_W  {

    private String name;





    private refac_C refac_c;




    private refac_A refac_a;


    public refac_W(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public refac_C getRefac_c() {
        return refac_c;
    }

    public void setRefac_c(refac_C refac_c) {
        this.refac_c = refac_c;
    }
    public refac_A getRefac_a() {
        return refac_a;
    }

    public void setRefac_a(refac_A refac_a) {
        this.refac_a = refac_a;
    }

}