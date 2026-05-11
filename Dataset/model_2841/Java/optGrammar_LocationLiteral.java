





import java.util.List;
import java.util.ArrayList;

public class optGrammar_LocationLiteral  {

    private String type;





    private optGrammar_NonArrayableDeclaration optgrammar_nonarrayabledeclaration;


    public optGrammar_LocationLiteral(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public optGrammar_NonArrayableDeclaration getOptgrammar_nonarrayabledeclaration() {
        return optgrammar_nonarrayabledeclaration;
    }

    public void setOptgrammar_nonarrayabledeclaration(optGrammar_NonArrayableDeclaration optgrammar_nonarrayabledeclaration) {
        this.optgrammar_nonarrayabledeclaration = optgrammar_nonarrayabledeclaration;
    }

}