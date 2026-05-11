





import java.util.List;
import java.util.ArrayList;

public class contentfwk_PhysicalDataComponent extends Element, DataComponent {






    private contentfwk_DataArchitecture contentfwk_dataarchitecture;




    private List<contentfwk_LogicalDataComponent> contentfwk_logicaldatacomponents;




    private contentfwk_LogicalDataComponent contentfwk_logicaldatacomponent;




    private contentfwk_PhysicalDataComponent contentfwk_physicaldatacomponent;


    public contentfwk_PhysicalDataComponent(
    ) {
        super(
        );
        this.contentfwk_logicaldatacomponents = new ArrayList<>();
    }

    public contentfwk_PhysicalDataComponent(
        ArrayList<contentfwk_LogicalDataComponent> contentfwk_logicaldatacomponents    ) {
        this.contentfwk_logicaldatacomponents = contentfwk_logicaldatacomponents;
    }


    public contentfwk_DataArchitecture getContentfwk_dataarchitecture() {
        return contentfwk_dataarchitecture;
    }

    public void setContentfwk_dataarchitecture(contentfwk_DataArchitecture contentfwk_dataarchitecture) {
        this.contentfwk_dataarchitecture = contentfwk_dataarchitecture;
    }
    public List<contentfwk_LogicalDataComponent> getContentfwk_logicaldatacomponents() {
        return contentfwk_logicaldatacomponents;
    }

    public void addContentfwk_logicaldatacomponent(Contentfwk_logicaldatacomponent contentfwk_logicaldatacomponent) {
        this.contentfwk_logicaldatacomponents.add(contentfwk_logicaldatacomponent);
    }
    public contentfwk_LogicalDataComponent getContentfwk_logicaldatacomponent() {
        return contentfwk_logicaldatacomponent;
    }

    public void setContentfwk_logicaldatacomponent(contentfwk_LogicalDataComponent contentfwk_logicaldatacomponent) {
        this.contentfwk_logicaldatacomponent = contentfwk_logicaldatacomponent;
    }
    public contentfwk_PhysicalDataComponent getContentfwk_physicaldatacomponent() {
        return contentfwk_physicaldatacomponent;
    }

    public void setContentfwk_physicaldatacomponent(contentfwk_PhysicalDataComponent contentfwk_physicaldatacomponent) {
        this.contentfwk_physicaldatacomponent = contentfwk_physicaldatacomponent;
    }

}