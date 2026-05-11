





import java.util.List;
import java.util.ArrayList;

public class dsml_web_PasswordField extends Field {

    private int size;
    private int maxlength;



    public dsml_web_PasswordField(
        int size,        int maxlength    ) {
        super(
        );
        this.size = size;
        this.maxlength = maxlength;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public int getMaxlength() {
        return maxlength;
    }

    public void setMaxlength(int maxlength) {
        this.maxlength = maxlength;
    }


}