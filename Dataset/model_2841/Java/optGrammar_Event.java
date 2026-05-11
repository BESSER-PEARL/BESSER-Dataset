





import java.util.List;
import java.util.ArrayList;

public class optGrammar_Event extends DefinitionBody {

    private String name;
    private boolean isAnonymous;



    public optGrammar_Event(
        String name,        boolean isAnonymous    ) {
        super(
        );
        this.name = name;
        this.isAnonymous = isAnonymous;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsanonymous() {
        return isAnonymous;
    }

    public void setIsanonymous(boolean isAnonymous) {
        this.isAnonymous = isAnonymous;
    }


}