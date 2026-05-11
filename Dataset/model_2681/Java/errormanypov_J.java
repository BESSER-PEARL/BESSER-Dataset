





import java.util.List;
import java.util.ArrayList;

public class errormanypov_J extends Named {






    private List<errormanypov_JK> errormanypov_jks;




    private errormanypov_A errormanypov_a;


    public errormanypov_J(
    ) {
        super(
        );
        this.errormanypov_jks = new ArrayList<>();
    }

    public errormanypov_J(
        ArrayList<errormanypov_JK> errormanypov_jks    ) {
        this.errormanypov_jks = errormanypov_jks;
    }


    public List<errormanypov_JK> getErrormanypov_jks() {
        return errormanypov_jks;
    }

    public void addErrormanypov_jk(Errormanypov_jk errormanypov_jk) {
        this.errormanypov_jks.add(errormanypov_jk);
    }
    public errormanypov_A getErrormanypov_a() {
        return errormanypov_a;
    }

    public void setErrormanypov_a(errormanypov_A errormanypov_a) {
        this.errormanypov_a = errormanypov_a;
    }

}