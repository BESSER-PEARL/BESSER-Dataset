





import java.util.List;
import java.util.ArrayList;

public class javaMM_TypeDeclaration extends AbstractTypeDeclaration {






    private List<javaMM_TypeParameter> javamm_typeparameters;


    public javaMM_TypeDeclaration(
    ) {
        super(
        );
        this.javamm_typeparameters = new ArrayList<>();
    }

    public javaMM_TypeDeclaration(
        ArrayList<javaMM_TypeParameter> javamm_typeparameters    ) {
        this.javamm_typeparameters = javamm_typeparameters;
    }


    public List<javaMM_TypeParameter> getJavamm_typeparameters() {
        return javamm_typeparameters;
    }

    public void addJavamm_typeparameter(Javamm_typeparameter javamm_typeparameter) {
        this.javamm_typeparameters.add(javamm_typeparameter);
    }

}