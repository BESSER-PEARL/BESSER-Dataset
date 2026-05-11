





import java.util.List;
import java.util.ArrayList;

public class classdiagram_TypedElement extends NamedElement {

    private boolean public;





    private classdiagram_Class classdiagram_class;


    public classdiagram_TypedElement(
        boolean public    ) {
        super(
        );
        this.public = public;
    }


    public boolean getPublic() {
        return public;
    }

    public void setPublic(boolean public) {
        this.public = public;
    }

    public classdiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(classdiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
    }

}