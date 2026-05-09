





import java.util.List;
import java.util.ArrayList;

public class javaMM_MethodRef extends ASTNode {






    private javaMM_TypeAccess javamm_typeaccess;




    private List<javaMM_MethodRefParameter> javamm_methodrefparameters;


    public javaMM_MethodRef(
    ) {
        super(
        );
        this.javamm_methodrefparameters = new ArrayList<>();
    }

    public javaMM_MethodRef(
        ArrayList<javaMM_MethodRefParameter> javamm_methodrefparameters    ) {
        this.javamm_methodrefparameters = javamm_methodrefparameters;
    }


    public javaMM_TypeAccess getJavamm_typeaccess() {
        return javamm_typeaccess;
    }

    public void setJavamm_typeaccess(javaMM_TypeAccess javamm_typeaccess) {
        this.javamm_typeaccess = javamm_typeaccess;
    }
    public List<javaMM_MethodRefParameter> getJavamm_methodrefparameters() {
        return javamm_methodrefparameters;
    }

    public void addJavamm_methodrefparameter(Javamm_methodrefparameter javamm_methodrefparameter) {
        this.javamm_methodrefparameters.add(javamm_methodrefparameter);
    }

}