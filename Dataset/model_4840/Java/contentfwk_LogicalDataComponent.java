





import java.util.List;
import java.util.ArrayList;

public class contentfwk_LogicalDataComponent extends DataComponent, Element {






    private contentfwk_DataEntity contentfwk_dataentity;




    private contentfwk_DataArchitecture contentfwk_dataarchitecture;




    private List<contentfwk_DataEntity> contentfwk_dataentitys;


    public contentfwk_LogicalDataComponent(
    ) {
        super(
        );
        this.contentfwk_dataentitys = new ArrayList<>();
    }

    public contentfwk_LogicalDataComponent(
        ArrayList<contentfwk_DataEntity> contentfwk_dataentitys    ) {
        this.contentfwk_dataentitys = contentfwk_dataentitys;
    }


    public contentfwk_DataEntity getContentfwk_dataentity() {
        return contentfwk_dataentity;
    }

    public void setContentfwk_dataentity(contentfwk_DataEntity contentfwk_dataentity) {
        this.contentfwk_dataentity = contentfwk_dataentity;
    }
    public contentfwk_DataArchitecture getContentfwk_dataarchitecture() {
        return contentfwk_dataarchitecture;
    }

    public void setContentfwk_dataarchitecture(contentfwk_DataArchitecture contentfwk_dataarchitecture) {
        this.contentfwk_dataarchitecture = contentfwk_dataarchitecture;
    }
    public List<contentfwk_DataEntity> getContentfwk_dataentitys() {
        return contentfwk_dataentitys;
    }

    public void addContentfwk_dataentity(Contentfwk_dataentity contentfwk_dataentity) {
        this.contentfwk_dataentitys.add(contentfwk_dataentity);
    }

}