





import java.util.List;
import java.util.ArrayList;

public class dsl_MethodDeclarator  {

    private String squareBrackets;
    private String id;





    private dsl_FormalParameters dsl_formalparameters;




    private dsl_MethodOrCtorDeclaration dsl_methodorctordeclaration;


    public dsl_MethodDeclarator(
        String squareBrackets,        String id    ) {
        this.squareBrackets = squareBrackets;
        this.id = id;
    }


    public String getSquarebrackets() {
        return squareBrackets;
    }

    public void setSquarebrackets(String squareBrackets) {
        this.squareBrackets = squareBrackets;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dsl_FormalParameters getDsl_formalparameters() {
        return dsl_formalparameters;
    }

    public void setDsl_formalparameters(dsl_FormalParameters dsl_formalparameters) {
        this.dsl_formalparameters = dsl_formalparameters;
    }
    public dsl_MethodOrCtorDeclaration getDsl_methodorctordeclaration() {
        return dsl_methodorctordeclaration;
    }

    public void setDsl_methodorctordeclaration(dsl_MethodOrCtorDeclaration dsl_methodorctordeclaration) {
        this.dsl_methodorctordeclaration = dsl_methodorctordeclaration;
    }

}