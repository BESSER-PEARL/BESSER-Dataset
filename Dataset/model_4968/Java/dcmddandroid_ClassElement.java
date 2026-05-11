





import java.util.List;
import java.util.ArrayList;

public class dcmddandroid_ClassElement extends EVisibility, NamedElement {

    private boolean final;
    private boolean static;



    public dcmddandroid_ClassElement(
        boolean final,        boolean static    ) {
        super(
        );
        this.final = final;
        this.static = static;
    }


    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }


}