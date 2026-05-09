





import java.util.List;
import java.util.ArrayList;

public class pivot_MessageType extends Type {






    private pivot_Operation pivot_operation;




    private pivot_Signal pivot_signal;


    public pivot_MessageType(
    ) {
        super(
        );
    }



    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }
    public pivot_Signal getPivot_signal() {
        return pivot_signal;
    }

    public void setPivot_signal(pivot_Signal pivot_signal) {
        this.pivot_signal = pivot_signal;
    }

}