





import java.util.List;
import java.util.ArrayList;

public class classLayout2Frontend_Enumeration extends PropertyType {






    private List<classLayout2Frontend_Literal> classlayout2frontend_literals;


    public classLayout2Frontend_Enumeration(
    ) {
        super(
        );
        this.classlayout2frontend_literals = new ArrayList<>();
    }

    public classLayout2Frontend_Enumeration(
        ArrayList<classLayout2Frontend_Literal> classlayout2frontend_literals    ) {
        this.classlayout2frontend_literals = classlayout2frontend_literals;
    }


    public List<classLayout2Frontend_Literal> getClasslayout2frontend_literals() {
        return classlayout2frontend_literals;
    }

    public void addClasslayout2frontend_literal(Classlayout2frontend_literal classlayout2frontend_literal) {
        this.classlayout2frontend_literals.add(classlayout2frontend_literal);
    }

}