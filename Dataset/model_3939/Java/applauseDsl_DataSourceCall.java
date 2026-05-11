





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_DataSourceCall  {

    private String name;





    private applauseDsl_RESTMethodCall applausedsl_restmethodcall;




    private applauseDsl_Screen applausedsl_screen;


    public applauseDsl_DataSourceCall(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public applauseDsl_RESTMethodCall getApplausedsl_restmethodcall() {
        return applausedsl_restmethodcall;
    }

    public void setApplausedsl_restmethodcall(applauseDsl_RESTMethodCall applausedsl_restmethodcall) {
        this.applausedsl_restmethodcall = applausedsl_restmethodcall;
    }
    public applauseDsl_Screen getApplausedsl_screen() {
        return applausedsl_screen;
    }

    public void setApplausedsl_screen(applauseDsl_Screen applausedsl_screen) {
        this.applausedsl_screen = applausedsl_screen;
    }

}