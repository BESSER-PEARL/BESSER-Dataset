





import java.util.List;
import java.util.ArrayList;

public class dsl_LocalVariableDeclaration  {

    private String finality;





    private dsl_Type dsl_type;




    private dsl_BlockStatement dsl_blockstatement;




    private List<dsl_VariableDeclarator> dsl_variabledeclarators;


    public dsl_LocalVariableDeclaration(
        String finality    ) {
        this.finality = finality;
        this.dsl_variabledeclarators = new ArrayList<>();
    }

    public dsl_LocalVariableDeclaration(
        String finality        ArrayList<dsl_VariableDeclarator> dsl_variabledeclarators    ) {
        this.finality = finality;
        this.dsl_variabledeclarators = dsl_variabledeclarators;
    }

    public String getFinality() {
        return finality;
    }

    public void setFinality(String finality) {
        this.finality = finality;
    }

    public dsl_Type getDsl_type() {
        return dsl_type;
    }

    public void setDsl_type(dsl_Type dsl_type) {
        this.dsl_type = dsl_type;
    }
    public dsl_BlockStatement getDsl_blockstatement() {
        return dsl_blockstatement;
    }

    public void setDsl_blockstatement(dsl_BlockStatement dsl_blockstatement) {
        this.dsl_blockstatement = dsl_blockstatement;
    }
    public List<dsl_VariableDeclarator> getDsl_variabledeclarators() {
        return dsl_variabledeclarators;
    }

    public void addDsl_variabledeclarator(Dsl_variabledeclarator dsl_variabledeclarator) {
        this.dsl_variabledeclarators.add(dsl_variabledeclarator);
    }

}