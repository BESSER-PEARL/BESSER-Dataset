





import java.util.List;
import java.util.ArrayList;

public class Triangles_AbstractClass  {

    private boolean flag;
    private int id;
    private String name;



    public Triangles_AbstractClass(
        boolean flag,        int id,        String name    ) {
        this.flag = flag;
        this.id = id;
        this.name = name;
    }


    public boolean getFlag() {
        return flag;
    }

    public void setFlag(boolean flag) {
        this.flag = flag;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}