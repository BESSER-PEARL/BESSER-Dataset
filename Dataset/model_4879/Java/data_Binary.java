





import java.util.List;
import java.util.ArrayList;

public class data_Binary extends Attachment {

    private String bytes;





    private data_InformationObject data_informationobject;


    public data_Binary(
        String bytes    ) {
        super(
        );
        this.bytes = bytes;
    }


    public String getBytes() {
        return bytes;
    }

    public void setBytes(String bytes) {
        this.bytes = bytes;
    }

    public data_InformationObject getData_informationobject() {
        return data_informationobject;
    }

    public void setData_informationobject(data_InformationObject data_informationobject) {
        this.data_informationobject = data_informationobject;
    }

}