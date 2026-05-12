





import java.util.List;
import java.util.ArrayList;

public class kbuild_MyVariable extends BuildEntry {

    private String name;





    private kbuild_Variable kbuild_variable;


    public kbuild_MyVariable(
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

    public kbuild_Variable getKbuild_variable() {
        return kbuild_variable;
    }

    public void setKbuild_variable(kbuild_Variable kbuild_variable) {
        this.kbuild_variable = kbuild_variable;
    }

}