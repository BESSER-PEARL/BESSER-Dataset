





import java.util.List;
import java.util.ArrayList;

public class myDsl_JsMethod  {

    private String name;
    private String type;





    private myDsl_Visualizer mydsl_visualizer;


    public myDsl_JsMethod(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public myDsl_Visualizer getMydsl_visualizer() {
        return mydsl_visualizer;
    }

    public void setMydsl_visualizer(myDsl_Visualizer mydsl_visualizer) {
        this.mydsl_visualizer = mydsl_visualizer;
    }

}