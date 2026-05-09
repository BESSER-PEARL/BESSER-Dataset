





import java.util.List;
import java.util.ArrayList;

public class simpleGraph_GraphElement  {

    private int id;
    private boolean generated;



    public simpleGraph_GraphElement(
        int id,        boolean generated    ) {
        this.id = id;
        this.generated = generated;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public boolean getGenerated() {
        return generated;
    }

    public void setGenerated(boolean generated) {
        this.generated = generated;
    }


}