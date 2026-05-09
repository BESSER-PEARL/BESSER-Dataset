





import java.util.List;
import java.util.ArrayList;

public class simpleworld101_Person  {

    private String name;
    private String foreName;



    public simpleworld101_Person(
        String name,        String foreName    ) {
        this.name = name;
        this.foreName = foreName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getForename() {
        return foreName;
    }

    public void setForename(String foreName) {
        this.foreName = foreName;
    }


}