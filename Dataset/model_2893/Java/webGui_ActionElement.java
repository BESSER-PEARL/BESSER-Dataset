





import java.util.List;
import java.util.ArrayList;

public class webGui_ActionElement extends PageElement {

    private String name;



    public webGui_ActionElement(
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