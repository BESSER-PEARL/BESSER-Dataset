





import java.util.List;
import java.util.ArrayList;

public class behaviour_NameLocationExpression extends LocationExpression {

    private String name;



    public behaviour_NameLocationExpression(
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