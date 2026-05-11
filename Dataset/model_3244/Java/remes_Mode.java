





import java.util.List;
import java.util.ArrayList;

public class remes_Mode  {

    private String name;
    private String initialization;



    public remes_Mode(
        String name,        String initialization    ) {
        this.name = name;
        this.initialization = initialization;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getInitialization() {
        return initialization;
    }

    public void setInitialization(String initialization) {
        this.initialization = initialization;
    }


}