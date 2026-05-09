





import java.util.List;
import java.util.ArrayList;

public class javaMM_ArrayCreation extends Expression {






    private javaMM_TypeAccess javamm_typeaccess;




    private javaMM_ArrayInitializer javamm_arrayinitializer;


    public javaMM_ArrayCreation(
    ) {
        super(
        );
    }



    public javaMM_TypeAccess getJavamm_typeaccess() {
        return javamm_typeaccess;
    }

    public void setJavamm_typeaccess(javaMM_TypeAccess javamm_typeaccess) {
        this.javamm_typeaccess = javamm_typeaccess;
    }
    public javaMM_ArrayInitializer getJavamm_arrayinitializer() {
        return javamm_arrayinitializer;
    }

    public void setJavamm_arrayinitializer(javaMM_ArrayInitializer javamm_arrayinitializer) {
        this.javamm_arrayinitializer = javamm_arrayinitializer;
    }

}