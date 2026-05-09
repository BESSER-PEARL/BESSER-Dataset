





import java.util.List;
import java.util.ArrayList;

public class model_Computer  {

    private String name;
    private String colors;



    public model_Computer(
        String name,        String colors    ) {
        this.name = name;
        this.colors = colors;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getColors() {
        return colors;
    }

    public void setColors(String colors) {
        this.colors = colors;
    }


}