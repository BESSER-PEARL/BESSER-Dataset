





import java.util.List;
import java.util.ArrayList;

public class b_SimpleCall  {






    private List<b_Arg> b_args;




    private b_Operation b_operation;


    public b_SimpleCall(
    ) {
        this.b_args = new ArrayList<>();
    }

    public b_SimpleCall(
        ArrayList<b_Arg> b_args    ) {
        this.b_args = b_args;
    }


    public List<b_Arg> getB_args() {
        return b_args;
    }

    public void addB_arg(B_arg b_arg) {
        this.b_args.add(b_arg);
    }
    public b_Operation getB_operation() {
        return b_operation;
    }

    public void setB_operation(b_Operation b_operation) {
        this.b_operation = b_operation;
    }

}