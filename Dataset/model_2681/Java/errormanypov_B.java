





import java.util.List;
import java.util.ArrayList;

public class errormanypov_B extends Named {






    private errormanypov_A errormanypov_a;




    private List<errormanypov_C> errormanypov_cs;


    public errormanypov_B(
    ) {
        super(
        );
        this.errormanypov_cs = new ArrayList<>();
    }

    public errormanypov_B(
        ArrayList<errormanypov_C> errormanypov_cs    ) {
        this.errormanypov_cs = errormanypov_cs;
    }


    public errormanypov_A getErrormanypov_a() {
        return errormanypov_a;
    }

    public void setErrormanypov_a(errormanypov_A errormanypov_a) {
        this.errormanypov_a = errormanypov_a;
    }
    public List<errormanypov_C> getErrormanypov_cs() {
        return errormanypov_cs;
    }

    public void addErrormanypov_c(Errormanypov_c errormanypov_c) {
        this.errormanypov_cs.add(errormanypov_c);
    }

}