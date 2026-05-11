





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_Variable extends Expression {

    private int name;



    public activitydiagram_Variable(
        int name    ) {
        super(
        );
        this.name = name;
    }


    public int getName() {
        return name;
    }

    public void setName(int name) {
        this.name = name;
    }


}