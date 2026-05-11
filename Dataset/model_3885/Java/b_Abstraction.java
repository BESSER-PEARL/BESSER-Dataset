





import java.util.List;
import java.util.ArrayList;

public class b_Abstraction  {

    private String name;





    private b_Imports b_imports;


    public b_Abstraction(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public b_Imports getB_imports() {
        return b_imports;
    }

    public void setB_imports(b_Imports b_imports) {
        this.b_imports = b_imports;
    }

}