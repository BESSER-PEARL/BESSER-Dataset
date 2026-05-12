





import java.util.List;
import java.util.ArrayList;

public class kbuild_ObjectVariable extends Value {

    private String additional;





    private kbuild_Variable kbuild_variable;


    public kbuild_ObjectVariable(
        String additional    ) {
        super(
        );
        this.additional = additional;
    }


    public String getAdditional() {
        return additional;
    }

    public void setAdditional(String additional) {
        this.additional = additional;
    }

    public kbuild_Variable getKbuild_variable() {
        return kbuild_variable;
    }

    public void setKbuild_variable(kbuild_Variable kbuild_variable) {
        this.kbuild_variable = kbuild_variable;
    }

}