





import java.util.List;
import java.util.ArrayList;

public class classdiagram_TypedElement extends NamedElement {

    private boolean public;





    private classdiagram_Typeable classdiagram_typeable;


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

    public classdiagram_Typeable getClassdiagram_typeable() {
        return classdiagram_typeable;
    }

    public void setClassdiagram_typeable(classdiagram_Typeable classdiagram_typeable) {
        this.classdiagram_typeable = classdiagram_typeable;
    }

}