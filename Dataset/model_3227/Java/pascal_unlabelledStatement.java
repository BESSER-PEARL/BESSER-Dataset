





import java.util.List;
import java.util.ArrayList;

public class pascal_unlabelledStatement  {






    private pascal_simpleStatement pascal_simplestatement;




    private pascal_structuredStatement pascal_structuredstatement;




    private pascal_statement pascal_statement;




    private pascal_parameterList pascal_parameterlist;




    private pascal_identifier pascal_identifier;


    public pascal_unlabelledStatement(
    ) {
    }



    public pascal_simpleStatement getPascal_simplestatement() {
        return pascal_simplestatement;
    }

    public void setPascal_simplestatement(pascal_simpleStatement pascal_simplestatement) {
        this.pascal_simplestatement = pascal_simplestatement;
    }
    public pascal_structuredStatement getPascal_structuredstatement() {
        return pascal_structuredstatement;
    }

    public void setPascal_structuredstatement(pascal_structuredStatement pascal_structuredstatement) {
        this.pascal_structuredstatement = pascal_structuredstatement;
    }
    public pascal_statement getPascal_statement() {
        return pascal_statement;
    }

    public void setPascal_statement(pascal_statement pascal_statement) {
        this.pascal_statement = pascal_statement;
    }
    public pascal_parameterList getPascal_parameterlist() {
        return pascal_parameterlist;
    }

    public void setPascal_parameterlist(pascal_parameterList pascal_parameterlist) {
        this.pascal_parameterlist = pascal_parameterlist;
    }
    public pascal_identifier getPascal_identifier() {
        return pascal_identifier;
    }

    public void setPascal_identifier(pascal_identifier pascal_identifier) {
        this.pascal_identifier = pascal_identifier;
    }

}