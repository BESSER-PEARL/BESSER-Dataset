





import java.util.List;
import java.util.ArrayList;

public class java__MethodRef extends ASTNode {






    private List<java__MethodRefParameter> java__methodrefparameters;




    private java__TypeAccess java__typeaccess;


    public java__MethodRef(
    ) {
        super(
        );
        this.java__methodrefparameters = new ArrayList<>();
    }

    public java__MethodRef(
        ArrayList<java__MethodRefParameter> java__methodrefparameters    ) {
        this.java__methodrefparameters = java__methodrefparameters;
    }


    public List<java__MethodRefParameter> getJava__methodrefparameters() {
        return java__methodrefparameters;
    }

    public void addJava__methodrefparameter(Java__methodrefparameter java__methodrefparameter) {
        this.java__methodrefparameters.add(java__methodrefparameter);
    }
    public java__TypeAccess getJava__typeaccess() {
        return java__typeaccess;
    }

    public void setJava__typeaccess(java__TypeAccess java__typeaccess) {
        this.java__typeaccess = java__typeaccess;
    }

}