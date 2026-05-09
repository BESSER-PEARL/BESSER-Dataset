





import java.util.List;
import java.util.ArrayList;

public class adaptiveSystem_Oclet  {

    private boolean wellFormed;
    private String orientation;
    private String quantor;
    private String name;





    private adaptiveSystem_AdaptiveSystem adaptivesystem_adaptivesystem;


    public adaptiveSystem_Oclet(
        boolean wellFormed,        String orientation,        String quantor,        String name    ) {
        this.wellFormed = wellFormed;
        this.orientation = orientation;
        this.quantor = quantor;
        this.name = name;
    }


    public boolean getWellformed() {
        return wellFormed;
    }

    public void setWellformed(boolean wellFormed) {
        this.wellFormed = wellFormed;
    }
    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public String getQuantor() {
        return quantor;
    }

    public void setQuantor(String quantor) {
        this.quantor = quantor;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public adaptiveSystem_AdaptiveSystem getAdaptivesystem_adaptivesystem() {
        return adaptivesystem_adaptivesystem;
    }

    public void setAdaptivesystem_adaptivesystem(adaptiveSystem_AdaptiveSystem adaptivesystem_adaptivesystem) {
        this.adaptivesystem_adaptivesystem = adaptivesystem_adaptivesystem;
    }

}