





import java.util.List;
import java.util.ArrayList;

public class express_expressions_VariableRef extends Primary {

    private String id;





    private NamedVariable namedvariable;


    public express_expressions_VariableRef(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public NamedVariable getNamedvariable() {
        return namedvariable;
    }

    public void setNamedvariable(NamedVariable namedvariable) {
        this.namedvariable = namedvariable;
    }

}