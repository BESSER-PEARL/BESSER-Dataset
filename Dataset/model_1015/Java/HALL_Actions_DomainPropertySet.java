





import java.util.List;
import java.util.ArrayList;

public class HALL_Actions_DomainPropertySet extends ActionMessageExpressionElement {

    private String name;



    public HALL_Actions_DomainPropertySet(
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