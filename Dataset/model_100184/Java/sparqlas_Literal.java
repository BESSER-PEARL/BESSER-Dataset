





import java.util.List;
import java.util.ArrayList;

public class sparqlas_Literal extends AbstractLiteral {

    private String lexicalForm;





    private sparqlas_Datatype sparqlas_datatype;


    public sparqlas_Literal(
        String lexicalForm    ) {
        super(
        );
        this.lexicalForm = lexicalForm;
    }


    public String getLexicalform() {
        return lexicalForm;
    }

    public void setLexicalform(String lexicalForm) {
        this.lexicalForm = lexicalForm;
    }

    public sparqlas_Datatype getSparqlas_datatype() {
        return sparqlas_datatype;
    }

    public void setSparqlas_datatype(sparqlas_Datatype sparqlas_datatype) {
        this.sparqlas_datatype = sparqlas_datatype;
    }

}