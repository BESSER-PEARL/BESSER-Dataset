





import java.util.List;
import java.util.ArrayList;

public class simpleal_Assign extends Stmt {

    private String name;





    private simpleal_Arith simpleal_arith;


    public simpleal_Assign(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simpleal_Arith getSimpleal_arith() {
        return simpleal_arith;
    }

    public void setSimpleal_arith(simpleal_Arith simpleal_arith) {
        this.simpleal_arith = simpleal_arith;
    }

}