





import java.util.List;
import java.util.ArrayList;

public class model_Instance extends Node {

    private String subPageID;



    public model_Instance(
        String subPageID    ) {
        super(
        );
        this.subPageID = subPageID;
    }


    public String getSubpageid() {
        return subPageID;
    }

    public void setSubpageid(String subPageID) {
        this.subPageID = subPageID;
    }


}