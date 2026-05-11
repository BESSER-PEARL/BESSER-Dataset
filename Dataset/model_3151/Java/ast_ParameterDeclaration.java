





import java.util.List;
import java.util.ArrayList;

public class ast_ParameterDeclaration extends CallableElement {

    private String name;



    public ast_ParameterDeclaration(
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