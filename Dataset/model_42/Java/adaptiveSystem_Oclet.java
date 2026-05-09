





import java.util.List;
import java.util.ArrayList;

public class adaptiveSystem_Oclet  {

    private String quantor;
    private String orientation;
    private String name;
    private boolean wellFormed;





    private adaptiveSystem_AdaptiveSystem adaptivesystem_adaptivesystem;


    public adaptiveSystem_Oclet(
        String quantor,        String orientation,        String name,        boolean wellFormed    ) {
        this.quantor = quantor;
        this.orientation = orientation;
        this.name = name;
        this.wellFormed = wellFormed;
    }


    public String getQuantor() {
        return quantor;
    }

    public void setQuantor(String quantor) {
        this.quantor = quantor;
    }
    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getWellformed() {
        return wellFormed;
    }

    public void setWellformed(boolean wellFormed) {
        this.wellFormed = wellFormed;
    }

    public adaptiveSystem_AdaptiveSystem getAdaptivesystem_adaptivesystem() {
        return adaptivesystem_adaptivesystem;
    }

    public void setAdaptivesystem_adaptivesystem(adaptiveSystem_AdaptiveSystem adaptivesystem_adaptivesystem) {
        this.adaptivesystem_adaptivesystem = adaptivesystem_adaptivesystem;
    }

}