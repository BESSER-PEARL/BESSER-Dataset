





import java.util.List;
import java.util.ArrayList;

public class contentfwk_PhysicalDataComponent extends Element, DataComponent {






    private contentfwk_LogicalDataComponent contentfwk_logicaldatacomponent;




    private List<contentfwk_LogicalDataComponent> contentfwk_logicaldatacomponents;




    private contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent;




    private contentfwk_PhysicalDataComponent contentfwk_physicaldatacomponent;




    private List<contentfwk_PhysicalApplicationComponent> contentfwk_physicalapplicationcomponents;


    public contentfwk_PhysicalDataComponent(
    ) {
        super(
        );
        this.contentfwk_logicaldatacomponents = new ArrayList<>();
        this.contentfwk_physicalapplicationcomponents = new ArrayList<>();
    }

    public contentfwk_PhysicalDataComponent(
        ArrayList<contentfwk_LogicalDataComponent> contentfwk_logicaldatacomponents,        ArrayList<contentfwk_PhysicalApplicationComponent> contentfwk_physicalapplicationcomponents    ) {
        this.contentfwk_logicaldatacomponents = contentfwk_logicaldatacomponents;
        this.contentfwk_physicalapplicationcomponents = contentfwk_physicalapplicationcomponents;
    }


    public contentfwk_LogicalDataComponent getContentfwk_logicaldatacomponent() {
        return contentfwk_logicaldatacomponent;
    }

    public void setContentfwk_logicaldatacomponent(contentfwk_LogicalDataComponent contentfwk_logicaldatacomponent) {
        this.contentfwk_logicaldatacomponent = contentfwk_logicaldatacomponent;
    }
    public List<contentfwk_LogicalDataComponent> getContentfwk_logicaldatacomponents() {
        return contentfwk_logicaldatacomponents;
    }

    public void addContentfwk_logicaldatacomponent(Contentfwk_logicaldatacomponent contentfwk_logicaldatacomponent) {
        this.contentfwk_logicaldatacomponents.add(contentfwk_logicaldatacomponent);
    }
    public contentfwk_PhysicalApplicationComponent getContentfwk_physicalapplicationcomponent() {
        return contentfwk_physicalapplicationcomponent;
    }

    public void setContentfwk_physicalapplicationcomponent(contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent) {
        this.contentfwk_physicalapplicationcomponent = contentfwk_physicalapplicationcomponent;
    }
    public contentfwk_PhysicalDataComponent getContentfwk_physicaldatacomponent() {
        return contentfwk_physicaldatacomponent;
    }

    public void setContentfwk_physicaldatacomponent(contentfwk_PhysicalDataComponent contentfwk_physicaldatacomponent) {
        this.contentfwk_physicaldatacomponent = contentfwk_physicaldatacomponent;
    }
    public List<contentfwk_PhysicalApplicationComponent> getContentfwk_physicalapplicationcomponents() {
        return contentfwk_physicalapplicationcomponents;
    }

    public void addContentfwk_physicalapplicationcomponent(Contentfwk_physicalapplicationcomponent contentfwk_physicalapplicationcomponent) {
        this.contentfwk_physicalapplicationcomponents.add(contentfwk_physicalapplicationcomponent);
    }

}