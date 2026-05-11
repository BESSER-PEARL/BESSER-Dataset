





import java.util.List;
import java.util.ArrayList;

public class becontent_Skin extends ViewItem {

    private String name;





    private becontent_Handler becontent_handler;


    public becontent_Skin(
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

    public becontent_Handler getBecontent_handler() {
        return becontent_handler;
    }

    public void setBecontent_handler(becontent_Handler becontent_handler) {
        this.becontent_handler = becontent_handler;
    }

}