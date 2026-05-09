





import java.util.List;
import java.util.ArrayList;

public class ast_SuperReference extends Expression {

    private String name;



    public ast_SuperReference(
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