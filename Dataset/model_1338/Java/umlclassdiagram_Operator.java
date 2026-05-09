





import java.util.List;
import java.util.ArrayList;

public class umlclassdiagram_Operator  {

    private String operator;





    private umlclassdiagram_Operation umlclassdiagram_operation;


    public umlclassdiagram_Operator(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public umlclassdiagram_Operation getUmlclassdiagram_operation() {
        return umlclassdiagram_operation;
    }

    public void setUmlclassdiagram_operation(umlclassdiagram_Operation umlclassdiagram_operation) {
        this.umlclassdiagram_operation = umlclassdiagram_operation;
    }

}