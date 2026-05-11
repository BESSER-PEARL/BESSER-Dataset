





import java.util.List;
import java.util.ArrayList;

public class myDsl_Variable_declarator  {

    private String nameVariable;
    private String lenVector;





    private myDsl_Variable_declaration mydsl_variable_declaration;




    private myDsl_Variable_declaration mydsl_variable_declaration;


    public myDsl_Variable_declarator(
        String nameVariable,        String lenVector    ) {
        this.nameVariable = nameVariable;
        this.lenVector = lenVector;
    }


    public String getNamevariable() {
        return nameVariable;
    }

    public void setNamevariable(String nameVariable) {
        this.nameVariable = nameVariable;
    }
    public String getLenvector() {
        return lenVector;
    }

    public void setLenvector(String lenVector) {
        this.lenVector = lenVector;
    }

    public myDsl_Variable_declaration getMydsl_variable_declaration() {
        return mydsl_variable_declaration;
    }

    public void setMydsl_variable_declaration(myDsl_Variable_declaration mydsl_variable_declaration) {
        this.mydsl_variable_declaration = mydsl_variable_declaration;
    }
    public myDsl_Variable_declaration getMydsl_variable_declaration() {
        return mydsl_variable_declaration;
    }

    public void setMydsl_variable_declaration(myDsl_Variable_declaration mydsl_variable_declaration) {
        this.mydsl_variable_declaration = mydsl_variable_declaration;
    }

}