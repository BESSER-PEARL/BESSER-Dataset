





import java.util.List;
import java.util.ArrayList;

public class iot2_Statement_For_Generic extends Statement {

    private String names;





    private iot2_Block iot2_block;




    private List<iot2_Expression> iot2_expressions;


    public iot2_Statement_For_Generic(
        String names    ) {
        super(
        );
        this.names = names;
        this.iot2_expressions = new ArrayList<>();
    }

    public iot2_Statement_For_Generic(
        String names        ArrayList<iot2_Expression> iot2_expressions    ) {
        this.names = names;
        this.iot2_expressions = iot2_expressions;
    }

    public String getNames() {
        return names;
    }

    public void setNames(String names) {
        this.names = names;
    }

    public iot2_Block getIot2_block() {
        return iot2_block;
    }

    public void setIot2_block(iot2_Block iot2_block) {
        this.iot2_block = iot2_block;
    }
    public List<iot2_Expression> getIot2_expressions() {
        return iot2_expressions;
    }

    public void addIot2_expression(Iot2_expression iot2_expression) {
        this.iot2_expressions.add(iot2_expression);
    }

}