





import java.util.List;
import java.util.ArrayList;

public class base_LiteralArray  {






    private List<base_Literal> base_literals;


    public base_LiteralArray(
    ) {
        this.base_literals = new ArrayList<>();
    }

    public base_LiteralArray(
        ArrayList<base_Literal> base_literals    ) {
        this.base_literals = base_literals;
    }


    public List<base_Literal> getBase_literals() {
        return base_literals;
    }

    public void addBase_literal(Base_literal base_literal) {
        this.base_literals.add(base_literal);
    }

}