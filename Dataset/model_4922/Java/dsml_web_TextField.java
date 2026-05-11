





import java.util.List;
import java.util.ArrayList;

public class dsml_web_TextField extends Field {

    private int maxlength;
    private int size;



    public dsml_web_TextField(
        int maxlength,        int size    ) {
        super(
        );
        this.maxlength = maxlength;
        this.size = size;
    }


    public int getMaxlength() {
        return maxlength;
    }

    public void setMaxlength(int maxlength) {
        this.maxlength = maxlength;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }


}