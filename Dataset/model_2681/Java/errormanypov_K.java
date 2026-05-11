





import java.util.List;
import java.util.ArrayList;

public class errormanypov_K extends Named {






    private errormanypov_C errormanypov_c;




    private List<errormanypov_M> errormanypov_ms;


    public errormanypov_K(
    ) {
        super(
        );
        this.errormanypov_ms = new ArrayList<>();
    }

    public errormanypov_K(
        ArrayList<errormanypov_M> errormanypov_ms    ) {
        this.errormanypov_ms = errormanypov_ms;
    }


    public errormanypov_C getErrormanypov_c() {
        return errormanypov_c;
    }

    public void setErrormanypov_c(errormanypov_C errormanypov_c) {
        this.errormanypov_c = errormanypov_c;
    }
    public List<errormanypov_M> getErrormanypov_ms() {
        return errormanypov_ms;
    }

    public void addErrormanypov_m(Errormanypov_m errormanypov_m) {
        this.errormanypov_ms.add(errormanypov_m);
    }

}