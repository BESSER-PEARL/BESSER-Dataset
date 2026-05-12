





import java.util.List;
import java.util.ArrayList;

public class Model_Transaction  {

    private String attribute;
    private None presenter;



    public Model_Transaction(
        String attribute,        None presenter    ) {
        this.attribute = attribute;
        this.presenter = presenter;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public None getPresenter() {
        return presenter;
    }

    public void setPresenter(None presenter) {
        this.presenter = presenter;
    }


}