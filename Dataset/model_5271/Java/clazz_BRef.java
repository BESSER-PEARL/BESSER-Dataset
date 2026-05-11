





import java.util.List;
import java.util.ArrayList;

public class clazz_BRef  {

    private String name;





    private clazz_B clazz_b;


    public clazz_BRef(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public clazz_B getClazz_b() {
        return clazz_b;
    }

    public void setClazz_b(clazz_B clazz_b) {
        this.clazz_b = clazz_b;
    }

}