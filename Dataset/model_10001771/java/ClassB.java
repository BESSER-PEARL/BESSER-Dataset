





import java.util.List;
import java.util.ArrayList;

public class ClassB  {

    private int attribute;





    private ClassA classa;


    public ClassB(
        int attribute    ) {
        this.attribute = attribute;
    }


    public int getAttribute() {
        return attribute;
    }

    public void setAttribute(int attribute) {
        this.attribute = attribute;
    }

    public ClassA getClassa() {
        return classa;
    }

    public void setClassa(ClassA classa) {
        this.classa = classa;
    }

}