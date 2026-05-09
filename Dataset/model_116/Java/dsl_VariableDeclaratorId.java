





import java.util.List;
import java.util.ArrayList;

public class dsl_VariableDeclaratorId  {

    private String id;
    private String squareBrackets;





    private dsl_VariableDeclarator dsl_variabledeclarator;




    private dsl_FormalParameter dsl_formalparameter;


    public dsl_VariableDeclaratorId(
        String id,        String squareBrackets    ) {
        this.id = id;
        this.squareBrackets = squareBrackets;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSquarebrackets() {
        return squareBrackets;
    }

    public void setSquarebrackets(String squareBrackets) {
        this.squareBrackets = squareBrackets;
    }

    public dsl_VariableDeclarator getDsl_variabledeclarator() {
        return dsl_variabledeclarator;
    }

    public void setDsl_variabledeclarator(dsl_VariableDeclarator dsl_variabledeclarator) {
        this.dsl_variabledeclarator = dsl_variabledeclarator;
    }
    public dsl_FormalParameter getDsl_formalparameter() {
        return dsl_formalparameter;
    }

    public void setDsl_formalparameter(dsl_FormalParameter dsl_formalparameter) {
        this.dsl_formalparameter = dsl_formalparameter;
    }

}