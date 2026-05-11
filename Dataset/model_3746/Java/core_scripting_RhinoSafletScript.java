





import java.util.List;
import java.util.ArrayList;

public class core_scripting_RhinoSafletScript extends SafletScript {

    private String rhinoScript;



    public core_scripting_RhinoSafletScript(
        String rhinoScript    ) {
        super(
        );
        this.rhinoScript = rhinoScript;
    }


    public String getRhinoscript() {
        return rhinoScript;
    }

    public void setRhinoscript(String rhinoScript) {
        this.rhinoScript = rhinoScript;
    }


}