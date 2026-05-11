





import java.util.List;
import java.util.ArrayList;

public class grammar_Node  {






    private grammar_ConnexionInstruction grammar_connexioninstruction;




    private grammar_LHS grammar_lhs;


    public grammar_Node(
    ) {
    }



    public grammar_ConnexionInstruction getGrammar_connexioninstruction() {
        return grammar_connexioninstruction;
    }

    public void setGrammar_connexioninstruction(grammar_ConnexionInstruction grammar_connexioninstruction) {
        this.grammar_connexioninstruction = grammar_connexioninstruction;
    }
    public grammar_LHS getGrammar_lhs() {
        return grammar_lhs;
    }

    public void setGrammar_lhs(grammar_LHS grammar_lhs) {
        this.grammar_lhs = grammar_lhs;
    }

}