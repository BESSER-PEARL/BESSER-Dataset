





import java.util.List;
import java.util.ArrayList;

public class model_ExternalDomainModel extends DomainModel_ {

    private String fileFormat;



    public model_ExternalDomainModel(
        String fileFormat    ) {
        super(
        );
        this.fileFormat = fileFormat;
    }


    public String getFileformat() {
        return fileFormat;
    }

    public void setFileformat(String fileFormat) {
        this.fileFormat = fileFormat;
    }


}