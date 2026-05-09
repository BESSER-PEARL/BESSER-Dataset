





import java.util.List;
import java.util.ArrayList;

public class kiamaas_Node  {

    private int deep;
    private int height;





    private kiamaas_Top kiamaas_top;


    public kiamaas_Node(
        int deep,        int height    ) {
        this.deep = deep;
        this.height = height;
    }


    public int getDeep() {
        return deep;
    }

    public void setDeep(int deep) {
        this.deep = deep;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }

    public kiamaas_Top getKiamaas_top() {
        return kiamaas_top;
    }

    public void setKiamaas_top(kiamaas_Top kiamaas_top) {
        this.kiamaas_top = kiamaas_top;
    }

}