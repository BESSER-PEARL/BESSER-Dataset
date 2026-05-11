





import java.util.List;
import java.util.ArrayList;

public class r1_TupleElementDefinition extends Element {

    private String name;





    private r1_TypeSpecifier r1_typespecifier;


    public r1_TupleElementDefinition(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public r1_TypeSpecifier getR1_typespecifier() {
        return r1_typespecifier;
    }

    public void setR1_typespecifier(r1_TypeSpecifier r1_typespecifier) {
        this.r1_typespecifier = r1_typespecifier;
    }

}