





import java.util.List;
import java.util.ArrayList;

public class pascal_set  {

    private String brackets;





    private pascal_factor pascal_factor;


    public pascal_set(
        String brackets    ) {
        this.brackets = brackets;
    }


    public String getBrackets() {
        return brackets;
    }

    public void setBrackets(String brackets) {
        this.brackets = brackets;
    }

    public pascal_factor getPascal_factor() {
        return pascal_factor;
    }

    public void setPascal_factor(pascal_factor pascal_factor) {
        this.pascal_factor = pascal_factor;
    }

}