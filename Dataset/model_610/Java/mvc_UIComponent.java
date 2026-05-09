





import java.util.List;
import java.util.ArrayList;

public class mvc_UIComponent extends Annotable {

    private String layout;
    private String name;
    private String type;
    private String id;





    private List<mvc_UIComponent> mvc_uicomponents;


    public mvc_UIComponent(
        String layout,        String name,        String type,        String id    ) {
        super(
        );
        this.layout = layout;
        this.name = name;
        this.type = type;
        this.id = id;
        this.mvc_uicomponents = new ArrayList<>();
    }

    public mvc_UIComponent(
        String layout,        String name,        String type,        String id        ArrayList<mvc_UIComponent> mvc_uicomponents    ) {
        this.layout = layout;
        this.name = name;
        this.type = type;
        this.id = id;
        this.mvc_uicomponents = mvc_uicomponents;
    }

    public String getLayout() {
        return layout;
    }

    public void setLayout(String layout) {
        this.layout = layout;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<mvc_UIComponent> getMvc_uicomponents() {
        return mvc_uicomponents;
    }

    public void addMvc_uicomponent(Mvc_uicomponent mvc_uicomponent) {
        this.mvc_uicomponents.add(mvc_uicomponent);
    }

}