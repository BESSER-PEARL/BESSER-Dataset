





import java.util.List;
import java.util.ArrayList;

public class limp_LocalProcedure extends Declaration, FunctionRef {

    private String name;





    private limp_VarBlock limp_varblock;


    public limp_LocalProcedure(
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

    public limp_VarBlock getLimp_varblock() {
        return limp_varblock;
    }

    public void setLimp_varblock(limp_VarBlock limp_varblock) {
        this.limp_varblock = limp_varblock;
    }

}