





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlUnaryExpression extends SadlExplicitValue {

    private String operator;





    private sADL_SadlExplicitValueLiteral sadl_sadlexplicitvalueliteral;


    public sADL_SadlUnaryExpression(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public sADL_SadlExplicitValueLiteral getSadl_sadlexplicitvalueliteral() {
        return sadl_sadlexplicitvalueliteral;
    }

    public void setSadl_sadlexplicitvalueliteral(sADL_SadlExplicitValueLiteral sadl_sadlexplicitvalueliteral) {
        this.sadl_sadlexplicitvalueliteral = sadl_sadlexplicitvalueliteral;
    }

}