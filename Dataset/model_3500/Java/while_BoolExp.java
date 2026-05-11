





import java.util.List;
import java.util.ArrayList;

public class while_BoolExp extends Exp {






    private while_If while_if;




    private while_While while_while;


    public while_BoolExp(
    ) {
        super(
        );
    }



    public while_If getWhile_if() {
        return while_if;
    }

    public void setWhile_if(while_If while_if) {
        this.while_if = while_if;
    }
    public while_While getWhile_while() {
        return while_while;
    }

    public void setWhile_while(while_While while_while) {
        this.while_while = while_while;
    }

}