





import java.util.List;
import java.util.ArrayList;

public class afpText_IOCAFunctionSetIdentification extends triplet {

    private String FCNSET;
    private String CATEGORY;



    public afpText_IOCAFunctionSetIdentification(
        String FCNSET,        String CATEGORY    ) {
        super(
        );
        this.FCNSET = FCNSET;
        this.CATEGORY = CATEGORY;
    }


    public String getFcnset() {
        return FCNSET;
    }

    public void setFcnset(String FCNSET) {
        this.FCNSET = FCNSET;
    }
    public String getCategory() {
        return CATEGORY;
    }

    public void setCategory(String CATEGORY) {
        this.CATEGORY = CATEGORY;
    }


}