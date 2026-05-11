





import java.util.List;
import java.util.ArrayList;

public class data_Image extends Attachment {

    private String height;
    private String width;





    private data_InformationObject data_informationobject;


    public data_Image(
        String height,        String width    ) {
        super(
        );
        this.height = height;
        this.width = width;
    }


    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }

    public data_InformationObject getData_informationobject() {
        return data_informationobject;
    }

    public void setData_informationobject(data_InformationObject data_informationobject) {
        this.data_informationobject = data_informationobject;
    }

}