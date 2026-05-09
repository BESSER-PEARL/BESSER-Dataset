





import java.util.List;
import java.util.ArrayList;

public class mvc_UILayout extends UIComponent {

    private String orientation;
    private int columns;





    private mvc_View mvc_view;




    private List<mvc_UIComponent> mvc_uicomponents;




    private List<mvc_View> mvc_views;


    public mvc_UILayout(
        String orientation,        int columns    ) {
        super(
        );
        this.orientation = orientation;
        this.columns = columns;
        this.mvc_uicomponents = new ArrayList<>();
        this.mvc_views = new ArrayList<>();
    }

    public mvc_UILayout(
        String orientation,        int columns        ArrayList<mvc_UIComponent> mvc_uicomponents,        ArrayList<mvc_View> mvc_views    ) {
        this.orientation = orientation;
        this.columns = columns;
        this.mvc_uicomponents = mvc_uicomponents;
        this.mvc_views = mvc_views;
    }

    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public int getColumns() {
        return columns;
    }

    public void setColumns(int columns) {
        this.columns = columns;
    }

    public mvc_View getMvc_view() {
        return mvc_view;
    }

    public void setMvc_view(mvc_View mvc_view) {
        this.mvc_view = mvc_view;
    }
    public List<mvc_UIComponent> getMvc_uicomponents() {
        return mvc_uicomponents;
    }

    public void addMvc_uicomponent(Mvc_uicomponent mvc_uicomponent) {
        this.mvc_uicomponents.add(mvc_uicomponent);
    }
    public List<mvc_View> getMvc_views() {
        return mvc_views;
    }

    public void addMvc_view(Mvc_view mvc_view) {
        this.mvc_views.add(mvc_view);
    }

}