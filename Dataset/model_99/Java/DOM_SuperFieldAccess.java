





import java.util.List;
import java.util.ArrayList;

public class DOM_SuperFieldAccess extends Expression {






    private Name name;




    private SimpleName simplename;


    public DOM_SuperFieldAccess(
    ) {
        super(
        );
    }



    public Name getName() {
        return name;
    }

    public void setName(Name name) {
        this.name = name;
    }
    public SimpleName getSimplename() {
        return simplename;
    }

    public void setSimplename(SimpleName simplename) {
        this.simplename = simplename;
    }

}