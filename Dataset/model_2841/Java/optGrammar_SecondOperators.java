





import java.util.List;
import java.util.ArrayList;

public class optGrammar_SecondOperators  {

    private String operator;





    private optGrammar_ArithmeticOperations optgrammar_arithmeticoperations;




    private optGrammar_PrimaryArithmetic optgrammar_primaryarithmetic;


    public optGrammar_SecondOperators(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public optGrammar_ArithmeticOperations getOptgrammar_arithmeticoperations() {
        return optgrammar_arithmeticoperations;
    }

    public void setOptgrammar_arithmeticoperations(optGrammar_ArithmeticOperations optgrammar_arithmeticoperations) {
        this.optgrammar_arithmeticoperations = optgrammar_arithmeticoperations;
    }
    public optGrammar_PrimaryArithmetic getOptgrammar_primaryarithmetic() {
        return optgrammar_primaryarithmetic;
    }

    public void setOptgrammar_primaryarithmetic(optGrammar_PrimaryArithmetic optgrammar_primaryarithmetic) {
        this.optgrammar_primaryarithmetic = optgrammar_primaryarithmetic;
    }

}