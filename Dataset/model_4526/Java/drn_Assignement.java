





import java.util.List;
import java.util.ArrayList;

public class drn_Assignement  {

    private String name;





    private List<drn_Parametre> drn_parametres;




    private List<drn_Expression> drn_expressions;




    private drn_Model drn_model;


    public drn_Assignement(
        String name    ) {
        this.name = name;
        this.drn_parametres = new ArrayList<>();
        this.drn_expressions = new ArrayList<>();
    }

    public drn_Assignement(
        String name        ArrayList<drn_Parametre> drn_parametres,        ArrayList<drn_Expression> drn_expressions    ) {
        this.name = name;
        this.drn_parametres = drn_parametres;
        this.drn_expressions = drn_expressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<drn_Parametre> getDrn_parametres() {
        return drn_parametres;
    }

    public void addDrn_parametre(Drn_parametre drn_parametre) {
        this.drn_parametres.add(drn_parametre);
    }
    public List<drn_Expression> getDrn_expressions() {
        return drn_expressions;
    }

    public void addDrn_expression(Drn_expression drn_expression) {
        this.drn_expressions.add(drn_expression);
    }
    public drn_Model getDrn_model() {
        return drn_model;
    }

    public void setDrn_model(drn_Model drn_model) {
        this.drn_model = drn_model;
    }

}