





import java.util.List;
import java.util.ArrayList;

public class adaptiveSystem_Node  {

    private String name;
    private String temp;
    private boolean disabledByAntiOclet;
    private boolean disabledByConflict;
    private boolean abstract;





    private adaptiveSystem_OccurrenceNet adaptivesystem_occurrencenet;


    public adaptiveSystem_Node(
        String name,        String temp,        boolean disabledByAntiOclet,        boolean disabledByConflict,        boolean abstract    ) {
        this.name = name;
        this.temp = temp;
        this.disabledByAntiOclet = disabledByAntiOclet;
        this.disabledByConflict = disabledByConflict;
        this.abstract = abstract;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTemp() {
        return temp;
    }

    public void setTemp(String temp) {
        this.temp = temp;
    }
    public boolean getDisabledbyantioclet() {
        return disabledByAntiOclet;
    }

    public void setDisabledbyantioclet(boolean disabledByAntiOclet) {
        this.disabledByAntiOclet = disabledByAntiOclet;
    }
    public boolean getDisabledbyconflict() {
        return disabledByConflict;
    }

    public void setDisabledbyconflict(boolean disabledByConflict) {
        this.disabledByConflict = disabledByConflict;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public adaptiveSystem_OccurrenceNet getAdaptivesystem_occurrencenet() {
        return adaptivesystem_occurrencenet;
    }

    public void setAdaptivesystem_occurrencenet(adaptiveSystem_OccurrenceNet adaptivesystem_occurrencenet) {
        this.adaptivesystem_occurrencenet = adaptivesystem_occurrencenet;
    }

}