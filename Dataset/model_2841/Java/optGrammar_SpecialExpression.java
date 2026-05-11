





import java.util.List;
import java.util.ArrayList;

public class optGrammar_SpecialExpression extends Expression {

    private String type;





    private List<optGrammar_Qualifier> optgrammar_qualifiers;




    private optGrammar_Field optgrammar_field;


    public optGrammar_SpecialExpression(
        String type    ) {
        super(
        );
        this.type = type;
        this.optgrammar_qualifiers = new ArrayList<>();
    }

    public optGrammar_SpecialExpression(
        String type        ArrayList<optGrammar_Qualifier> optgrammar_qualifiers    ) {
        this.type = type;
        this.optgrammar_qualifiers = optgrammar_qualifiers;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<optGrammar_Qualifier> getOptgrammar_qualifiers() {
        return optgrammar_qualifiers;
    }

    public void addOptgrammar_qualifier(Optgrammar_qualifier optgrammar_qualifier) {
        this.optgrammar_qualifiers.add(optgrammar_qualifier);
    }
    public optGrammar_Field getOptgrammar_field() {
        return optgrammar_field;
    }

    public void setOptgrammar_field(optGrammar_Field optgrammar_field) {
        this.optgrammar_field = optgrammar_field;
    }

}