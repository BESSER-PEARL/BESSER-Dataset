





import java.util.List;
import java.util.ArrayList;

public class jkind_TypeDef  {

    private String name;





    private jkind_File jkind_file;


    public jkind_TypeDef(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public jkind_File getJkind_file() {
        return jkind_file;
    }

    public void setJkind_file(jkind_File jkind_file) {
        this.jkind_file = jkind_file;
    }

}