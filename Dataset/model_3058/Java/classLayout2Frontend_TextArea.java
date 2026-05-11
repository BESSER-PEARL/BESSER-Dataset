





import java.util.List;
import java.util.ArrayList;

public class classLayout2Frontend_TextArea extends Output {

    private boolean isTitle;
    private String value;



    public classLayout2Frontend_TextArea(
        boolean isTitle,        String value    ) {
        super(
        );
        this.isTitle = isTitle;
        this.value = value;
    }


    public boolean getIstitle() {
        return isTitle;
    }

    public void setIstitle(boolean isTitle) {
        this.isTitle = isTitle;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}