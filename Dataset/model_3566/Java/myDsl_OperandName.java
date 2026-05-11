





import java.util.List;
import java.util.ArrayList;

public class myDsl_OperandName  {

    private String id;





    private myDsl_Operand mydsl_operand;


    public myDsl_OperandName(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public myDsl_Operand getMydsl_operand() {
        return mydsl_operand;
    }

    public void setMydsl_operand(myDsl_Operand mydsl_operand) {
        this.mydsl_operand = mydsl_operand;
    }

}