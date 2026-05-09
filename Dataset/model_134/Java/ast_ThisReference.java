





import java.util.List;
import java.util.ArrayList;

public class ast_ThisReference extends Expression {

    private String name;



    public ast_ThisReference(
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