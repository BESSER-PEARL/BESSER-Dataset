





import java.util.List;
import java.util.ArrayList;

public class HibernateTest_Bz356181_Main  {

    private String nonTransient;
    private String transient;



    public HibernateTest_Bz356181_Main(
        String nonTransient,        String transient    ) {
        this.nonTransient = nonTransient;
        this.transient = transient;
    }


    public String getNontransient() {
        return nonTransient;
    }

    public void setNontransient(String nonTransient) {
        this.nonTransient = nonTransient;
    }
    public String getTransient() {
        return transient;
    }

    public void setTransient(String transient) {
        this.transient = transient;
    }


}