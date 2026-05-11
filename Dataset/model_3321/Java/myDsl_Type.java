





import java.util.List;
import java.util.ArrayList;

public class myDsl_Type  {

    private String typeVector;





    private myDsl_Method_declaration mydsl_method_declaration;




    private myDsl_Variable_declaration mydsl_variable_declaration;


    public myDsl_Type(
        String typeVector    ) {
        this.typeVector = typeVector;
    }


    public String getTypevector() {
        return typeVector;
    }

    public void setTypevector(String typeVector) {
        this.typeVector = typeVector;
    }

    public myDsl_Method_declaration getMydsl_method_declaration() {
        return mydsl_method_declaration;
    }

    public void setMydsl_method_declaration(myDsl_Method_declaration mydsl_method_declaration) {
        this.mydsl_method_declaration = mydsl_method_declaration;
    }
    public myDsl_Variable_declaration getMydsl_variable_declaration() {
        return mydsl_variable_declaration;
    }

    public void setMydsl_variable_declaration(myDsl_Variable_declaration mydsl_variable_declaration) {
        this.mydsl_variable_declaration = mydsl_variable_declaration;
    }

}