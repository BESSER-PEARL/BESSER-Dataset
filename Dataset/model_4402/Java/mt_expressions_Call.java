





import java.util.List;
import java.util.ArrayList;

public class mt_expressions_Call extends ASTNode {

    private String name;
    private String prefix;



    public mt_expressions_Call(
        String name,        String prefix    ) {
        super(
        );
        this.name = name;
        this.prefix = prefix;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }


}