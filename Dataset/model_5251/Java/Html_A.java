





import java.util.List;
import java.util.ArrayList;

public class Html_A extends BODYElement {

    private String name;
    private String ahref;



    public Html_A(
        String name,        String ahref    ) {
        super(
        );
        this.name = name;
        this.ahref = ahref;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAhref() {
        return ahref;
    }

    public void setAhref(String ahref) {
        this.ahref = ahref;
    }


}