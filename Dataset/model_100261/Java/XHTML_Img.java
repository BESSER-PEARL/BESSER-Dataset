





import java.util.List;
import java.util.ArrayList;

public class XHTML_Img extends Attrs, Special, EMPTY {

    private String ismap;



    public XHTML_Img(
        String ismap    ) {
        super(
        );
        this.ismap = ismap;
    }


    public String getIsmap() {
        return ismap;
    }

    public void setIsmap(String ismap) {
        this.ismap = ismap;
    }


}