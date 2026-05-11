





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_ScreenSection  {

    private String title;





    private applauseDsl_DataSourceCall applausedsl_datasourcecall;




    private applauseDsl_ScreenSectionItems applausedsl_screensectionitems;




    private applauseDsl_Screen applausedsl_screen;


    public applauseDsl_ScreenSection(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public applauseDsl_DataSourceCall getApplausedsl_datasourcecall() {
        return applausedsl_datasourcecall;
    }

    public void setApplausedsl_datasourcecall(applauseDsl_DataSourceCall applausedsl_datasourcecall) {
        this.applausedsl_datasourcecall = applausedsl_datasourcecall;
    }
    public applauseDsl_ScreenSectionItems getApplausedsl_screensectionitems() {
        return applausedsl_screensectionitems;
    }

    public void setApplausedsl_screensectionitems(applauseDsl_ScreenSectionItems applausedsl_screensectionitems) {
        this.applausedsl_screensectionitems = applausedsl_screensectionitems;
    }
    public applauseDsl_Screen getApplausedsl_screen() {
        return applausedsl_screen;
    }

    public void setApplausedsl_screen(applauseDsl_Screen applausedsl_screen) {
        this.applausedsl_screen = applausedsl_screen;
    }

}