





import java.util.List;
import java.util.ArrayList;

public class wappm_IndexPage extends DynamicPage {

    private int size;



    public wappm_IndexPage(
        int size    ) {
        super(
        );
        this.size = size;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }


}