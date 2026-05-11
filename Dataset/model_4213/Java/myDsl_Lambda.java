





import java.util.List;
import java.util.ArrayList;

public class myDsl_Lambda extends Expression {

    private String name;



    public myDsl_Lambda(
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