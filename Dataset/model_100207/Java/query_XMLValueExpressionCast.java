





import java.util.List;
import java.util.ArrayList;

public class query_XMLValueExpressionCast extends ValueExpressionCast {

    private String passingMechanism;



    public query_XMLValueExpressionCast(
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