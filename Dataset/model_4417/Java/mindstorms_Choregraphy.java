





import java.util.List;
import java.util.ArrayList;

public class mindstorms_Choregraphy extends Flow {

    private String name;





    private mindstorms_Reuse mindstorms_reuse;


    public mindstorms_Choregraphy(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mindstorms_Reuse getMindstorms_reuse() {
        return mindstorms_reuse;
    }

    public void setMindstorms_reuse(mindstorms_Reuse mindstorms_reuse) {
        this.mindstorms_reuse = mindstorms_reuse;
    }

}