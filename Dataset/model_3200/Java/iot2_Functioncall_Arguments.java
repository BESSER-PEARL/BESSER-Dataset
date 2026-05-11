





import java.util.List;
import java.util.ArrayList;

public class iot2_Functioncall_Arguments  {






    private List<iot2_Expression> iot2_expressions;


    public iot2_Functioncall_Arguments(
    ) {
        this.iot2_expressions = new ArrayList<>();
    }

    public iot2_Functioncall_Arguments(
        ArrayList<iot2_Expression> iot2_expressions    ) {
        this.iot2_expressions = iot2_expressions;
    }


    public List<iot2_Expression> getIot2_expressions() {
        return iot2_expressions;
    }

    public void addIot2_expression(Iot2_expression iot2_expression) {
        this.iot2_expressions.add(iot2_expression);
    }

}