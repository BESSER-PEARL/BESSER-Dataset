





import java.util.List;
import java.util.ArrayList;

public class query_XMLQueryArgumentItem extends QueryValueExpression {

    private String passingMechanism;



    public query_XMLQueryArgumentItem(
        String passingMechanism    ) {
        super(
        );
        this.passingMechanism = passingMechanism;
    }


    public String getPassingmechanism() {
        return passingMechanism;
    }

    public void setPassingmechanism(String passingMechanism) {
        this.passingMechanism = passingMechanism;
    }


}