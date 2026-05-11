





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_UIAction  {

    private int order;
    private String title;
    private String icon;
    private String gesture;





    private applauseDsl_ScreenListItemCell applausedsl_screenlistitemcell;




    private applauseDsl_Screen applausedsl_screen;




    private applauseDsl_UIActionSpecification applausedsl_uiactionspecification;


    public applauseDsl_UIAction(
        int order,        String title,        String icon,        String gesture    ) {
        this.order = order;
        this.title = title;
        this.icon = icon;
        this.gesture = gesture;
    }


    public int getOrder() {
        return order;
    }

    public void setOrder(int order) {
        this.order = order;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public String getGesture() {
        return gesture;
    }

    public void setGesture(String gesture) {
        this.gesture = gesture;
    }

    public applauseDsl_ScreenListItemCell getApplausedsl_screenlistitemcell() {
        return applausedsl_screenlistitemcell;
    }

    public void setApplausedsl_screenlistitemcell(applauseDsl_ScreenListItemCell applausedsl_screenlistitemcell) {
        this.applausedsl_screenlistitemcell = applausedsl_screenlistitemcell;
    }
    public applauseDsl_Screen getApplausedsl_screen() {
        return applausedsl_screen;
    }

    public void setApplausedsl_screen(applauseDsl_Screen applausedsl_screen) {
        this.applausedsl_screen = applausedsl_screen;
    }
    public applauseDsl_UIActionSpecification getApplausedsl_uiactionspecification() {
        return applausedsl_uiactionspecification;
    }

    public void setApplausedsl_uiactionspecification(applauseDsl_UIActionSpecification applausedsl_uiactionspecification) {
        this.applausedsl_uiactionspecification = applausedsl_uiactionspecification;
    }

}