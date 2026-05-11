





import java.util.List;
import java.util.ArrayList;

public class kmLogo_ProcCall extends Expression {






    private kmLogo_ProcDeclaration kmlogo_procdeclaration;




    private kmLogo_ProcDeclaration kmlogo_procdeclaration;




    private List<kmLogo_Expression> kmlogo_expressions;


    public kmLogo_ProcCall(
    ) {
        super(
        );
        this.kmlogo_expressions = new ArrayList<>();
    }

    public kmLogo_ProcCall(
        ArrayList<kmLogo_Expression> kmlogo_expressions    ) {
        this.kmlogo_expressions = kmlogo_expressions;
    }


    public kmLogo_ProcDeclaration getKmlogo_procdeclaration() {
        return kmlogo_procdeclaration;
    }

    public void setKmlogo_procdeclaration(kmLogo_ProcDeclaration kmlogo_procdeclaration) {
        this.kmlogo_procdeclaration = kmlogo_procdeclaration;
    }
    public kmLogo_ProcDeclaration getKmlogo_procdeclaration() {
        return kmlogo_procdeclaration;
    }

    public void setKmlogo_procdeclaration(kmLogo_ProcDeclaration kmlogo_procdeclaration) {
        this.kmlogo_procdeclaration = kmlogo_procdeclaration;
    }
    public List<kmLogo_Expression> getKmlogo_expressions() {
        return kmlogo_expressions;
    }

    public void addKmlogo_expression(Kmlogo_expression kmlogo_expression) {
        this.kmlogo_expressions.add(kmlogo_expression);
    }

}