





import java.util.List;
import java.util.ArrayList;

public class optGrammar_Contract  {

    private String name;





    private optGrammar_Model optgrammar_model;




    private optGrammar_NewExpression optgrammar_newexpression;




    private List<optGrammar_DefinitionBody> optgrammar_definitionbodys;


    public optGrammar_Contract(
        String name    ) {
        this.name = name;
        this.optgrammar_definitionbodys = new ArrayList<>();
    }

    public optGrammar_Contract(
        String name        ArrayList<optGrammar_DefinitionBody> optgrammar_definitionbodys    ) {
        this.name = name;
        this.optgrammar_definitionbodys = optgrammar_definitionbodys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public optGrammar_Model getOptgrammar_model() {
        return optgrammar_model;
    }

    public void setOptgrammar_model(optGrammar_Model optgrammar_model) {
        this.optgrammar_model = optgrammar_model;
    }
    public optGrammar_NewExpression getOptgrammar_newexpression() {
        return optgrammar_newexpression;
    }

    public void setOptgrammar_newexpression(optGrammar_NewExpression optgrammar_newexpression) {
        this.optgrammar_newexpression = optgrammar_newexpression;
    }
    public List<optGrammar_DefinitionBody> getOptgrammar_definitionbodys() {
        return optgrammar_definitionbodys;
    }

    public void addOptgrammar_definitionbody(Optgrammar_definitionbody optgrammar_definitionbody) {
        this.optgrammar_definitionbodys.add(optgrammar_definitionbody);
    }

}