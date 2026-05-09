





import java.util.List;
import java.util.ArrayList;

public class simpleGraph_GraphElement  {

    private boolean generated;
    private int id;



    public simpleGraph_GraphElement(
        boolean generated,        int id    ) {
        this.generated = generated;
        this.id = id;
    }


    public boolean getGenerated() {
        return generated;
    }

    public void setGenerated(boolean generated) {
        this.generated = generated;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}