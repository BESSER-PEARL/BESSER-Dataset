





import java.util.List;
import java.util.ArrayList;

public class r1_AggregateExpression extends Expression {

    private String path;



    public r1_AggregateExpression(
        String path    ) {
        super(
        );
        this.path = path;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }


}