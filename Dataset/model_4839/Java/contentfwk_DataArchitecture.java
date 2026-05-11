





import java.util.List;
import java.util.ArrayList;

public class contentfwk_DataArchitecture extends Architecture {






    private List<contentfwk_LogicalDataComponent> contentfwk_logicaldatacomponents;




    private List<contentfwk_PhysicalDataComponent> contentfwk_physicaldatacomponents;


    public contentfwk_DataArchitecture(
    ) {
        super(
        );
        this.contentfwk_logicaldatacomponents = new ArrayList<>();
        this.contentfwk_physicaldatacomponents = new ArrayList<>();
    }

    public contentfwk_DataArchitecture(
        ArrayList<contentfwk_LogicalDataComponent> contentfwk_logicaldatacomponents,        ArrayList<contentfwk_PhysicalDataComponent> contentfwk_physicaldatacomponents    ) {
        this.contentfwk_logicaldatacomponents = contentfwk_logicaldatacomponents;
        this.contentfwk_physicaldatacomponents = contentfwk_physicaldatacomponents;
    }


    public List<contentfwk_LogicalDataComponent> getContentfwk_logicaldatacomponents() {
        return contentfwk_logicaldatacomponents;
    }

    public void addContentfwk_logicaldatacomponent(Contentfwk_logicaldatacomponent contentfwk_logicaldatacomponent) {
        this.contentfwk_logicaldatacomponents.add(contentfwk_logicaldatacomponent);
    }
    public List<contentfwk_PhysicalDataComponent> getContentfwk_physicaldatacomponents() {
        return contentfwk_physicaldatacomponents;
    }

    public void addContentfwk_physicaldatacomponent(Contentfwk_physicaldatacomponent contentfwk_physicaldatacomponent) {
        this.contentfwk_physicaldatacomponents.add(contentfwk_physicaldatacomponent);
    }

}