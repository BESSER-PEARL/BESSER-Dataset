





import java.util.List;
import java.util.ArrayList;

public class egt_ColorRegistry  {

    private String images;





    private egt_GraphModel egt_graphmodel;


    public egt_ColorRegistry(
        String images    ) {
        this.images = images;
    }


    public String getImages() {
        return images;
    }

    public void setImages(String images) {
        this.images = images;
    }

    public egt_GraphModel getEgt_graphmodel() {
        return egt_graphmodel;
    }

    public void setEgt_graphmodel(egt_GraphModel egt_graphmodel) {
        this.egt_graphmodel = egt_graphmodel;
    }

}