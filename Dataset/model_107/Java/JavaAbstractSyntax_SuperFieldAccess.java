





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_SuperFieldAccess extends Expression {






    private SimpleName simplename;




    private Name name;


    public JavaAbstractSyntax_SuperFieldAccess(
    ) {
        super(
        );
    }



    public SimpleName getSimplename() {
        return simplename;
    }

    public void setSimplename(SimpleName simplename) {
        this.simplename = simplename;
    }
    public Name getName() {
        return name;
    }

    public void setName(Name name) {
        this.name = name;
    }

}