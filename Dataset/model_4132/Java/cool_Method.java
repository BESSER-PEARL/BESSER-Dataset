





import java.util.List;
import java.util.ArrayList;

public class cool_Method extends Feature_ {






    private cool_Type cool_type;




    private List<cool_Formal> cool_formals;


    public cool_Method(
    ) {
        super(
        );
        this.cool_formals = new ArrayList<>();
    }

    public cool_Method(
        ArrayList<cool_Formal> cool_formals    ) {
        this.cool_formals = cool_formals;
    }


    public cool_Type getCool_type() {
        return cool_type;
    }

    public void setCool_type(cool_Type cool_type) {
        this.cool_type = cool_type;
    }
    public List<cool_Formal> getCool_formals() {
        return cool_formals;
    }

    public void addCool_formal(Cool_formal cool_formal) {
        this.cool_formals.add(cool_formal);
    }

}