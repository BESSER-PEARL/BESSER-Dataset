





import java.util.List;
import java.util.ArrayList;

public class while_l_Program  {






    private List<while_l_Function> while_l_functions;




    private while_l_Wh while_l_wh;


    public while_l_Program(
    ) {
        this.while_l_functions = new ArrayList<>();
    }

    public while_l_Program(
        ArrayList<while_l_Function> while_l_functions    ) {
        this.while_l_functions = while_l_functions;
    }


    public List<while_l_Function> getWhile_l_functions() {
        return while_l_functions;
    }

    public void addWhile_l_function(While_l_function while_l_function) {
        this.while_l_functions.add(while_l_function);
    }
    public while_l_Wh getWhile_l_wh() {
        return while_l_wh;
    }

    public void setWhile_l_wh(while_l_Wh while_l_wh) {
        this.while_l_wh = while_l_wh;
    }

}