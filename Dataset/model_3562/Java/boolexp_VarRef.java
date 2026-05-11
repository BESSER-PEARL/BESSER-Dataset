





import java.util.List;
import java.util.ArrayList;

public class boolexp_VarRef extends Exp {

    private String name;



    public boolexp_VarRef(
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


}