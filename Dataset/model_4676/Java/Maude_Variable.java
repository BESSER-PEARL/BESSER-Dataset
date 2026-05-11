





import java.util.List;
import java.util.ArrayList;

public class Maude_Variable extends Term {

    private String name;



    public Maude_Variable(
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