





import java.util.List;
import java.util.ArrayList;

public class superimposed_NavigationCallExp extends PropertyCallExp {

    private String name;



    public superimposed_NavigationCallExp(
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