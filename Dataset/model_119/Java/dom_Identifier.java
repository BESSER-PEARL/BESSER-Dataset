





import java.util.List;
import java.util.ArrayList;

public class dom_Identifier extends IProperty, IPropertyName, IPropertySelector, Node {

    private String name;



    public dom_Identifier(
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