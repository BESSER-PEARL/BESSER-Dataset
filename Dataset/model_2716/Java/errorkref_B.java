





import java.util.List;
import java.util.ArrayList;

public class errorkref_B  {

    private String id;





    private errorkref_L1 errorkref_l1;




    private errorkref_A errorkref_a;


    public errorkref_B(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public errorkref_L1 getErrorkref_l1() {
        return errorkref_l1;
    }

    public void setErrorkref_l1(errorkref_L1 errorkref_l1) {
        this.errorkref_l1 = errorkref_l1;
    }
    public errorkref_A getErrorkref_a() {
        return errorkref_a;
    }

    public void setErrorkref_a(errorkref_A errorkref_a) {
        this.errorkref_a = errorkref_a;
    }

}