





import java.util.List;
import java.util.ArrayList;

public class sadl_ContentList  {

    private String annContent;





    private sadl_ModelName sadl_modelname;


    public sadl_ContentList(
        String annContent    ) {
        this.annContent = annContent;
    }


    public String getAnncontent() {
        return annContent;
    }

    public void setAnncontent(String annContent) {
        this.annContent = annContent;
    }

    public sadl_ModelName getSadl_modelname() {
        return sadl_modelname;
    }

    public void setSadl_modelname(sadl_ModelName sadl_modelname) {
        this.sadl_modelname = sadl_modelname;
    }

}