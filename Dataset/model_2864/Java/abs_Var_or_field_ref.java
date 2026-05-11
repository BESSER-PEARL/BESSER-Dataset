





import java.util.List;
import java.util.ArrayList;

public class abs_Var_or_field_ref extends Pure_exp {

    private String name;



    public abs_Var_or_field_ref(
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