





import java.util.List;
import java.util.ArrayList;

public class Statement  {






    private cobol_statements_Condition cobol_statements_condition;




    private cobol_statements_NestedStatement cobol_statements_nestedstatement;




    private cobol_sentences_StatementContainer cobol_sentences_statementcontainer;




    private cobol_statements_Statement cobol_statements_statement;




    private cobol_sections_DataDivisionSection cobol_sections_datadivisionsection;


    public Statement(
    ) {
    }



    public cobol_statements_Condition getCobol_statements_condition() {
        return cobol_statements_condition;
    }

    public void setCobol_statements_condition(cobol_statements_Condition cobol_statements_condition) {
        this.cobol_statements_condition = cobol_statements_condition;
    }
    public cobol_statements_NestedStatement getCobol_statements_nestedstatement() {
        return cobol_statements_nestedstatement;
    }

    public void setCobol_statements_nestedstatement(cobol_statements_NestedStatement cobol_statements_nestedstatement) {
        this.cobol_statements_nestedstatement = cobol_statements_nestedstatement;
    }
    public cobol_sentences_StatementContainer getCobol_sentences_statementcontainer() {
        return cobol_sentences_statementcontainer;
    }

    public void setCobol_sentences_statementcontainer(cobol_sentences_StatementContainer cobol_sentences_statementcontainer) {
        this.cobol_sentences_statementcontainer = cobol_sentences_statementcontainer;
    }
    public cobol_statements_Statement getCobol_statements_statement() {
        return cobol_statements_statement;
    }

    public void setCobol_statements_statement(cobol_statements_Statement cobol_statements_statement) {
        this.cobol_statements_statement = cobol_statements_statement;
    }
    public cobol_sections_DataDivisionSection getCobol_sections_datadivisionsection() {
        return cobol_sections_datadivisionsection;
    }

    public void setCobol_sections_datadivisionsection(cobol_sections_DataDivisionSection cobol_sections_datadivisionsection) {
        this.cobol_sections_datadivisionsection = cobol_sections_datadivisionsection;
    }

}