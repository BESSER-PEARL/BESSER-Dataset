





import java.util.List;
import java.util.ArrayList;

public class B_Predicate extends Expression {






    private B_Operation b_operation;




    private B_Any b_any;




    private B_Machine b_machine;


    public B_Predicate(
    ) {
        super(
        );
    }



    public B_Operation getB_operation() {
        return b_operation;
    }

    public void setB_operation(B_Operation b_operation) {
        this.b_operation = b_operation;
    }
    public B_Any getB_any() {
        return b_any;
    }

    public void setB_any(B_Any b_any) {
        this.b_any = b_any;
    }
    public B_Machine getB_machine() {
        return b_machine;
    }

    public void setB_machine(B_Machine b_machine) {
        this.b_machine = b_machine;
    }

}