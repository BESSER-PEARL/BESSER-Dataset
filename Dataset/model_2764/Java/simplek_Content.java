





import java.util.List;
import java.util.ArrayList;

public class simplek_Content  {

    private String name;





    private simplek_Base simplek_base;


    public simplek_Content(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simplek_Base getSimplek_base() {
        return simplek_base;
    }

    public void setSimplek_base(simplek_Base simplek_base) {
        this.simplek_base = simplek_base;
    }

}