





import java.util.List;
import java.util.ArrayList;

public class errormanypov_JK extends Named {






    private List<errormanypov_K> errormanypov_ks;


    public errormanypov_JK(
    ) {
        super(
        );
        this.errormanypov_ks = new ArrayList<>();
    }

    public errormanypov_JK(
        ArrayList<errormanypov_K> errormanypov_ks    ) {
        this.errormanypov_ks = errormanypov_ks;
    }


    public List<errormanypov_K> getErrormanypov_ks() {
        return errormanypov_ks;
    }

    public void addErrormanypov_k(Errormanypov_k errormanypov_k) {
        this.errormanypov_ks.add(errormanypov_k);
    }

}