





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppNamedElement extends CppModelElement {

    private String name;



    public Metamodelo_Cpp_CppNamedElement(
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