





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_Layout extends Control {

    private String type;





    private List<appBuilderDSL_Control> appbuilderdsl_controls;




    private appBuilderDSL_View appbuilderdsl_view;




    private appBuilderDSL_CompositeScreen appbuilderdsl_compositescreen;


    public appBuilderDSL_Layout(
        String type    ) {
        super(
        );
        this.type = type;
        this.appbuilderdsl_controls = new ArrayList<>();
    }

    public appBuilderDSL_Layout(
        String type        ArrayList<appBuilderDSL_Control> appbuilderdsl_controls    ) {
        this.type = type;
        this.appbuilderdsl_controls = appbuilderdsl_controls;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<appBuilderDSL_Control> getAppbuilderdsl_controls() {
        return appbuilderdsl_controls;
    }

    public void addAppbuilderdsl_control(Appbuilderdsl_control appbuilderdsl_control) {
        this.appbuilderdsl_controls.add(appbuilderdsl_control);
    }
    public appBuilderDSL_View getAppbuilderdsl_view() {
        return appbuilderdsl_view;
    }

    public void setAppbuilderdsl_view(appBuilderDSL_View appbuilderdsl_view) {
        this.appbuilderdsl_view = appbuilderdsl_view;
    }
    public appBuilderDSL_CompositeScreen getAppbuilderdsl_compositescreen() {
        return appbuilderdsl_compositescreen;
    }

    public void setAppbuilderdsl_compositescreen(appBuilderDSL_CompositeScreen appbuilderdsl_compositescreen) {
        this.appbuilderdsl_compositescreen = appbuilderdsl_compositescreen;
    }

}