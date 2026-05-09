





import java.util.List;
import java.util.ArrayList;

public class adaptiveSystem_Node  {

    private String temp;
    private boolean abstract;
    private boolean disabledByConflict;
    private boolean disabledByAntiOclet;
    private String name;





    private adaptiveSystem_OccurrenceNet adaptivesystem_occurrencenet;


    public adaptiveSystem_Node(
        String temp,        boolean abstract,        boolean disabledByConflict,        boolean disabledByAntiOclet,        String name    ) {
        this.temp = temp;
        this.abstract = abstract;
        this.disabledByConflict = disabledByConflict;
        this.disabledByAntiOclet = disabledByAntiOclet;
        this.name = name;
    }


    public String getTemp() {
        return temp;
    }

    public void setTemp(String temp) {
        this.temp = temp;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getDisabledbyconflict() {
        return disabledByConflict;
    }

    public void setDisabledbyconflict(boolean disabledByConflict) {
        this.disabledByConflict = disabledByConflict;
    }
    public boolean getDisabledbyantioclet() {
        return disabledByAntiOclet;
    }

    public void setDisabledbyantioclet(boolean disabledByAntiOclet) {
        this.disabledByAntiOclet = disabledByAntiOclet;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public adaptiveSystem_OccurrenceNet getAdaptivesystem_occurrencenet() {
        return adaptivesystem_occurrencenet;
    }

    public void setAdaptivesystem_occurrencenet(adaptiveSystem_OccurrenceNet adaptivesystem_occurrencenet) {
        this.adaptivesystem_occurrencenet = adaptivesystem_occurrencenet;
    }

}