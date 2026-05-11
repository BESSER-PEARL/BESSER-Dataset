





import java.util.List;
import java.util.ArrayList;

public class errormanypov_A extends Named {






    private List<errormanypov_E> errormanypov_es;


    public errormanypov_A(
    ) {
        super(
        );
        this.errormanypov_es = new ArrayList<>();
    }

    public errormanypov_A(
        ArrayList<errormanypov_E> errormanypov_es    ) {
        this.errormanypov_es = errormanypov_es;
    }


    public List<errormanypov_E> getErrormanypov_es() {
        return errormanypov_es;
    }

    public void addErrormanypov_e(Errormanypov_e errormanypov_e) {
        this.errormanypov_es.add(errormanypov_e);
    }

}