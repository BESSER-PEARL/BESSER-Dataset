





import java.util.List;
import java.util.ArrayList;

public class stext_InterfaceScope extends Scope {

    private String name;



    public stext_InterfaceScope(
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